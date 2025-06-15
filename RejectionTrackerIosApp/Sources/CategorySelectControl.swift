//
//  CategorySelectControl.swift
//  Rejected
//
//  Created by Ian MacCallum on 6/14/25.
//

import SwiftUI
import SwiftData

struct CategorySelectControl: View {
    @Binding var selectedCategory: Category?
    @State private var showingCategoryPicker = false
    @State private var showingCreateCategoryView = false
    @Environment(\.parraTheme) var parraTheme
    @Query var categories: [Category]

    let onComplete: (Category) -> Void

    @State private var createCategoryViewHeight: CGFloat = 300

    var body: some View {
        HStack {
            if let category = selectedCategory {
                Button(action: {
                    showingCategoryPicker = true
                }) {
                    HStack {
                        IconView(icon: category.decodedIcon())

                        Text(category.name)
                            .foregroundColor(.primary)
                        Spacer()

                        if category.id == selectedCategory?.id {
                            Image(systemName: "checkmark")
                                .foregroundColor(.blue)
                        }
                    }
                }
                .padding(6)
            } else {
                Button(action: {
                    if categories.isEmpty {
                        showingCreateCategoryView = true
                    } else {
                        showingCategoryPicker = true
                    }
                }) {
                    HStack {
                        Text("Select category")
                            .foregroundColor(.gray.opacity(0.5))
                        Spacer()
                    }
                }
                .frame(maxWidth: .infinity)
                .padding()
            }

            Spacer()
        }
        .background(parraTheme.palette.primaryBackground.toParraColor())
        .cornerRadius(10)
        .sheet(isPresented: $showingCategoryPicker) {
            CategoryPickerView(selectedCategory: $selectedCategory, onComplete: onComplete) {
                showingCategoryPicker = false
            }
        }
        .sheet(isPresented: $showingCreateCategoryView) {
            CreateCategoryView(
                onComplete: { category in
                    selectedCategory = category
                    onComplete(category)
                },
                onClose: {
                    showingCreateCategoryView = false
                })
            .fixedSize(horizontal: false, vertical: true)
            .modifier(GetHeightModifier(height: $createCategoryViewHeight))
            .presentationDetents([.height(createCategoryViewHeight)])
            .presentationDragIndicator(.visible)
        }
    }
}


