//
//  Rejection.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import SwiftData

@Model
class Rejection: Identifiable {
    var id: UUID

    @Relationship(deleteRule: .nullify) var category: Category?
    var title: String
    var note: String?
    var createdAt: Date

    init(category: Category, title: String, note: String? = nil) {
        self.id = UUID()
        self.category = category
        self.title = title
        self.note = note
        self.createdAt = Date()
    }
}
