//
//  PreviewContainer.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/20/24.
//

import Foundation
import SwiftData

@MainActor
let previewContainer: ModelContainer =  {
    do {
        let container = try ModelContainer(for: Category.self, Rejection.self, configurations: ModelConfiguration(isStoredInMemoryOnly: true))


        return container
    } catch {
        fatalError()
    }
}()
