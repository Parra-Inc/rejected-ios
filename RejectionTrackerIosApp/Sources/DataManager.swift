//
//  DataManager.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import SwiftData

extension ModelContext {
//
//    // MARK: - Rejection Functions
//
    @MainActor
    @discardableResult
    func createRejection(category: Category, title: String, note: String?) -> Rejection {
        let newRejection = Rejection(category: category, title: title, note: note)
        self.insert(newRejection)
        saveContext()
        return newRejection
    }

    @MainActor
    func updateRejection(_ rejection: Rejection, category: Category, title: String, note: String?) {
        rejection.category = category
        rejection.title = title
        rejection.note = note
        saveContext()
    }

    @MainActor
    func deleteRejection(_ rejection: Rejection) {
        self.delete(rejection)
        saveContext()
    }

    // MARK: - Category Functions
    @MainActor
    func createCategory(icon: Icon?, name: String) -> Category {
        let newCategory = try! Category(icon: icon, name: name)
        self.insert(newCategory)
        saveContext()
        return newCategory
    }

    @MainActor
    func updateCategory(_ category: Category, icon: Icon?, name: String) {
        category.icon = try! JSONEncoder().encode(icon)
        category.name = name
        saveContext()
    }

    @MainActor
    func deleteCategory(_ category: Category) {
        self.delete(category)
        category.rejections?.forEach { rejection in
            rejection.category = nil
        }
        saveContext()
    }

    // MARK: - Helper Functions

    @MainActor
    private func saveContext() {
        do {
//            try self.save()
            print("Saved context")
        } catch {
            print("Error saving context: \(error)")
        }
    }
}
