//
//  Category.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import SwiftData

@Model
class Category: Identifiable {
    var id: UUID
    var icon: Data?
    var name: String
    var createdAt: Date

    @Relationship(deleteRule: .nullify, inverse: \Rejection.category) var rejections: [Rejection]?


    init(icon: Icon?, name: String) {
        self.id = UUID()
        self.icon = try! JSONEncoder().encode(icon)
        self.name = name
        self.createdAt = Date()
    }

    func decodedIcon() -> Icon? {
        guard let iconData = icon else { return nil }
        return try! JSONDecoder().decode(Icon.self, from: iconData)
    }
}

