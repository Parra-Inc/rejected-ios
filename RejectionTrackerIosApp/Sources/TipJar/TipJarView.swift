//
//  TipJarView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import StoreKit

struct TipJarView: View {
    @Binding var isPresented: Bool
    @State private var storeManager = StoreManager()
    @State private var animatedEmoji = "🙏"
    private let emojiOptions = ["🙏", "❤️", "✨", "💖"]

    var body: some View {
        VStack(spacing: 30) {
            Spacer()

            VStack(spacing: 24) {
                animatedEmojiView

                Text("Karma is a 😸")
                    .font(.title2)
                    .fontWeight(.bold)

                Text("If this stupid little app put a smile on your face please consider tipping. Every contribution, no matter how small, makes a big difference!")
                    .font(.body)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal)
            }

            Spacer()

            VStack(spacing: 15) {
                Text("Buy some karma!")
                    .font(.caption)
                    .foregroundColor(.gray.opacity(0.5))
                if let error = storeManager.error {
                    Text("Something went wrong: \(error.localizedDescription)")
                        .font(.caption)
                        .foregroundColor(.red.opacity(70))
                        .padding(.vertical, 10)
                }
                ForEach(storeManager.products, id: \.self) { product in
                    TipButton(
                        emoji: emojiForProduct(product),
                        product: product
                    ) {
                        Task {
                            do {
                                try await storeManager.purchase(product)
                            } catch {
                                print("Failed to purchase: \(error)")
                            }
                        }
                    }
                }
            }

            LargeButton(title: "Maybe Later", style: .secondary) {
                isPresented = false
            }
        }
        .presentationDragIndicator(.visible)
        .safeAreaPadding()
        .task {
            await storeManager.requestProducts()
        }
    }

    private var animatedEmojiView: some View {
        Text(animatedEmoji)
            .font(.system(size: 80))
            .onAppear {
                animateEmoji()
            }
    }

    private func animateEmoji() {
        Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
            withAnimation {
                animatedEmoji = emojiOptions.randomElement() ?? "🙏"
            }
        }
    }

    private func emojiForProduct(_ product: Product) -> String {
        switch product.id {
        case "v1.tip.1":
            return "☕️"
        case "v1.tip.3":
            return "🍕"
        case "v1.tip.10":
            return "🎉"
        default:
            return "💰"
        }
    }
}

struct TipButton: View {
    let emoji: String
    let product: Product
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack {
                Text(emoji)
                    .font(.largeTitle)
                Text(product.displayPrice)
                    .font(.headline)
            }
            .frame(maxWidth: .infinity)
            .padding()
            .background(.blue.opacity(0.1))
            .foregroundColor(.blue)
            .cornerRadius(10)
        }
    }
}
