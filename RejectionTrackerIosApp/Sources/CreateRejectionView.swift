//
//  CreateRejectionView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import SwiftData

struct CreateRejectionView: View {
    @State private var category: Category?
    @State private var title = ""
    @State private var note = ""
    @State private var showCategoryError = false
    @State private var showTitleError = false

    @Environment(\.parraTheme) var parraTheme
    @Environment(\.modelContext) var modelContext

    @State private var scrollInsetBottom: CGFloat = 44 // Estimate

    let onComplete: (_ rejection: Rejection) -> Void
    let onClose: () -> Void

    var body: some View {
        NavigationView {
            ZStack {
                ScrollView {
                    VStack {
                        FormControl(
                            title: "Category",
                            error: showCategoryError ? "Please select a category" : nil) {
                                CategorySelectControl(selectedCategory: $category, onComplete: { category in
                                    clearCategoryError()
                                })
                            }

                        FormControl(
                            title: "Title",
                            error: showTitleError ? "Please enter a title" : nil) {
                                TextField("Enter a title", text: $title)
                                    .padding()
                                    .background(parraTheme.palette.primaryBackground.toParraColor())
                                    .cornerRadius(10)
                            }

                        FormControl(
                            title: "Note") {
                                TextEditor(text: $note)

                                    .scrollContentBackground(.hidden)
                                    .frame(height: 100)
                                    .padding()
                                    .background(parraTheme.palette.primaryBackground.toParraColor())
                                    .cornerRadius(10)
                            }
                    }
                    .padding(16)
                }
                .safeAreaInset(edge: .bottom, spacing: 0) {
                    // some bottom-sticked content, or just –
                    Spacer()
                        .frame(height: scrollInsetBottom)
                }


                VStack {
                    Spacer()

                    LargeButton(title: "Save Rejection", action: validateAndSave)
                    .padding(.horizontal)
                    .padding(.vertical, 20)
                    .background {
                        GeometryReader { geometry in
                            LinearGradient(
                                gradient: Gradient(colors: [.white.opacity(0), .white, .white]),
                                startPoint: .top,
                                endPoint: .bottom
                            )
                            .task {
                                scrollInsetBottom = geometry.size.height
                            }
                        }
                    }
                }
            }
            .navigationTitle("Add Rejection")
            .toolbar {
                ToolbarItem(placement: .automatic) {
                    Button {
                        onClose()
                    } label: {
                        Image(systemName: "xmark")
                    }
                }
            }
        }
    }

    @MainActor private func validateAndSave() {
        showCategoryError = category == nil
        showTitleError = title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty


        if !showCategoryError && !showTitleError {
            saveRejection()
        }
    }

    private func clearCategoryError() {
        showCategoryError = false
    }

    @MainActor private func saveRejection() {
        if let category = category {
            let rejection = modelContext.createRejection(
                category: category,
                title: title,
                note: note
            )
            onComplete(rejection)
        }
    }
}
#Preview {

    CreateRejectionView {rejection in } onClose: {

    }
}
