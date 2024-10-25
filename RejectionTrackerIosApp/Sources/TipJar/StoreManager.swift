//
//  StoreManager.swift
//  Rejected
//
//  Created by Mick MacCallum on 10/25/24.
//

import SwiftUI
import StoreKit

@Observable
class StoreManager {
    enum StoreError: Error {
        case failedVerification
        case userCancelled
        case pending
        case unknown
    }

    var products: [Product] = []
    var error: Error?
    var purchasedProducts = [Product]()

    private var updateListenerTask: Task<Void, Error>? = nil

    init() {
        updateListenerTask = listenForTransactions()
    }

    deinit {
        updateListenerTask?.cancel()
    }

    @MainActor
    func requestProducts() async {
        print("Fetching products")

        self.error = nil

        do {
            let storeProducts = try await Product.products(for: ["v1.tip.1", "v1.tip.3", "v1.tip.10"])
            products = storeProducts.sorted(by: { $0.price < $1.price })
            print("Finished fetching \(storeProducts.count) product(s)")
        } catch {
            self.error = error
            print("Failed to load products: \(error)")
        }
    }

    private func listenForTransactions() -> Task<Void, Error> {
        return Task.detached {
            for await result in Transaction.updates {
                do {
                    let transaction = try self.checkVerified(result)

                    // Handle transaction here
                    await self.handleTransaction(transaction)

                    // Finish the transaction
                    await transaction.finish()
                } catch {
                    print("Transaction failed verification: \(error)")
                }
            }
        }
    }

    @MainActor
    func purchase(_ product: Product) async throws {
        let result = try await product.purchase()

        switch result {
        case .success(let verification):
            let transaction = try checkVerified(verification)
            await handleTransaction(transaction)
            await transaction.finish()
        case .userCancelled:
            throw StoreError.userCancelled
        case .pending:
            throw StoreError.pending
        @unknown default:
            throw StoreError.unknown
        }
    }

    // 6. Handle the transaction
    @MainActor
    private func handleTransaction(_ transaction: StoreKit.Transaction) async {
        // Handle transaction based on the product type
        let productId = transaction.productID

        if transaction.productType == .nonConsumable {
            // Handle one-time purchase
            if let product = products.first(where: { $0.id == productId }) {
                purchasedProducts.append(product)
            }
        } else if transaction.productType == .autoRenewable {
            // Handle subscription
            if let product = products.first(where: { $0.id == productId }) {
                purchasedProducts.append(product)
            }
        }

        // Save the transaction information locally
        await updatePurchaseState(productId: productId)
    }

    // 7. Verify the transaction
    private func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
        switch result {
        case .unverified:
            throw StoreError.failedVerification
        case .verified(let safe):
            return safe
        }
    }

    // 8. Update local purchase state
    @MainActor
    private func updatePurchaseState(productId: String) async {
        // Check current entitlements
        for await result in Transaction.currentEntitlements {
            do {
                let transaction = try checkVerified(result)

                if transaction.productID == productId {
                    if let product = products.first(where: { $0.id == productId }) {
                        purchasedProducts.append(product)
                    }
                }
            } catch {
                print("Failed to verify transaction: \(error)")
            }
        }
    }
}


