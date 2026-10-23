//
//  CategoryPickerView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import SwiftData
import SwipeActions

struct CategoryRow: View {
    let category: Category

    @Environment(\.parraTheme) var parraTheme

    var body: some View {
        HStack {
            IconView(icon: category.decodedIcon())
                .accessibilityHidden(true)

            Text(category.name)
                .font(.headline)
                .fontWeight(.semibold)

            Spacer()
        }
        .padding(10)
        .background(parraTheme.palette.primaryBackground.toParraColor())
    }
}


struct CategoryPickerView: View {

    @State private var showingCreateCategoryView = false
    @State private var scrollInsetBottom: CGFloat = 44 // Estimate
    @State var state: SwipeState = .untouched // <= HERE

    @Environment(\.dismiss) private var dismiss
    @Environment(\.parraTheme) var parraTheme
    @Environment(\.modelContext) var modelContext
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    @State private var createCategoryViewHeight: CGFloat = 300

    @Binding var selectedCategory: Category?

    let onComplete: (Category) -> Void
    let onClose: () -> Void

    @Query(sort: \Category.createdAt) var categories: [Category]

    var body: some View {
        NavigationView {
            ZStack {
                ScrollView {

                    VStack(spacing: 6) {
                        ForEach(categories) { category in
                            Button {
                                selectedCategory = category
                                dismiss()
                            } label: {
                                HStack {
                                    IconView(icon: category.decodedIcon())
                                        .accessibilityHidden(true)
                                    //
                                    Text(category.name)
                                        .foregroundColor(.primary)
                                    Spacer()

                                    if category.id == selectedCategory?.id {
                                        Image(systemName: "checkmark")
                                            .foregroundColor(.blue)
                                            .accessibilityHidden(true)
                                    }
                                }
                                .frame(maxWidth: .infinity)
                                .padding(10)
                                .background(parraTheme.palette.primaryBackground.toParraColor())
                                .addFullSwipeAction(
                                    menu: .slided,
                                    swipeColor: .red, state: $state) { // <= Color is the same as last button in Trailing for full effect
                                        Leading {
                                        }
                                        Trailing {

                                            Button {
                                                animatedDelete(category)
                                            } label: {
                                                Image(systemName: "trash")
                                                    .foregroundColor(.white)
                                            }
                                            .accessibilityLabel("Delete category")
                                            .contentShape(Rectangle())
                                            .frame(width: 60)
                                            .frame(maxHeight: .infinity)
                                            .background(Color.red) // <=== Look here
                                        }
                                    } action: { // <= action for full swiping
                                        animatedDelete(category)
                                    }

                            }
                            .frame(maxWidth: .infinity)
                            .cornerRadius(10)
                            .contextMenu {
                                Button(role: .destructive) {
                                    animatedDelete(category)
                                } label: {
                                    Label("Delete category", systemImage: "trash")
                                }
                            }
                            .accessibilityAddTraits(category.id == selectedCategory?.id ? .isSelected : [])
                            .accessibilityAction(named: "Delete category") {
                                deleteCategory(category)
                            }
                        }
                    }
                    .safeAreaPadding()
                    .safeAreaInset(edge: .bottom, spacing: 0) {
                        // some bottom-sticked content, or just –
                        Spacer()
                            .frame(height: scrollInsetBottom)
                    }
                }

                VStack {
                    Spacer()

                    LargeButton(title: "Add Category") {
                        showingCreateCategoryView = true
                    }
                    .padding(.horizontal)
                    .padding(.vertical, 20)
                    .background {
                        GeometryReader { geometry in
                            LinearGradient(
                                gradient: Gradient(colors: [Color(.systemBackground).opacity(0), Color(.systemBackground), Color(.systemBackground)]),
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
            .navigationTitle("Category")
            .toolbar {
                ToolbarItem(placement: .automatic) {
                    Button {
                        onClose()
                    } label: {
                        Image(systemName: "xmark")
                    }
                    .accessibilityLabel("Close")
                }
            }
        }
        .presentationDetents([.medium, .large])
        .sheet(isPresented: $showingCreateCategoryView) {
            CreateCategoryView(onComplete: { category in
                selectedCategory = category
                dismiss()
                onComplete(category)
            }, onClose: {
                showingCreateCategoryView = false
            })
            .fixedSize(horizontal: false, vertical: true)
            .modifier(GetHeightModifier(height: $createCategoryViewHeight))
            .presentationDetents([.height(createCategoryViewHeight)])
            .presentationDragIndicator(.visible)
        }
    }

    private func animatedDelete(_ category: Category) {
        let animation: SwiftUI.Animation? = reduceMotion ? nil : SwiftUI.Animation.easeInOut
        withAnimation(animation) {
            deleteCategory(category)
        }
    }

    private func deleteCategory(_ category: Category) {
        modelContext.deleteCategory(category)

        if selectedCategory == category {
            selectedCategory = nil
        }
    }
}
