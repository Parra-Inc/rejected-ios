//
//  CreateCategoryView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI
import EmojiPicker
import Smile

struct CreateCategoryView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var name = ""
    @State private var icon: Icon?
    @State var selectedEmoji: Emoji?

    @State private var showNameError = false
    @State private var showingIconOptions = false
    @State private var showingEmojiPicker = false
    @State private var showingUrlInput = false
    @State private var urlInput = ""
    @Environment(\.parraTheme) var parraTheme
    @Environment(\.modelContext) var modelContext

    let onComplete: (_ category: Category) -> Void

    var body: some View {
        NavigationView {
            ZStack {
                VStack {
                    FormControl {
                        HStack {
                            Menu {
                                Section {
                                    Button(action: {
                                        showingEmojiPicker = true
                                    }) {
                                        Text("Emoji")
                                    }

                                    Button("Image") {
                                        showingUrlInput = true
                                    }
                                }

                                Divider()

                                if icon != nil {
                                    Button("Remove", role: .destructive) {
                                        icon = nil
                                    }
                                }

                            } label: {
                                IconView(icon: icon, size: .xl, context: .add)
                            }

                            Spacer()
                        }
                    }

                    FormControl(title: "Name", error: showNameError ? "Name is required" : nil) {
                        TextField("Enter category name", text: $name)
                            .padding()
                            .background(parraTheme.palette.primaryBackground.toParraColor())
                            .cornerRadius(10)
                    }

                    Spacer()
                }
                .padding()

                VStack {
                    Spacer()
                    LargeButton(title: "Save Category", action: saveCategory)
                        .padding(.horizontal)
                        .padding(.bottom, 20)
                }
            }
            .navigationTitle("Add Category")
            .sheet(isPresented: $showingEmojiPicker) {
                NavigationView {
                    EmojiPickerView(
                        selectedEmoji: .init(get: {
                            guard case .emoji(let emoji) = icon else {
                                return nil
                            }

                            return Emoji(value: emoji, description: Smile.name(emoji: emoji).first ?? "")
                        }, set: { emoji in
                            guard let emoji = emoji else {
                                icon = nil
                                return
                            }

                            icon = .emoji(value: emoji.value)
                        }),
                        selectedColor: .gray.opacity(0.2),
                        emojiBackgroundColor: parraTheme.palette.primaryBackground.toParraColor(),
                        emojiCornerRadius: 10
                    )
                    .navigationTitle("Emojis")
                    .navigationBarTitleDisplayMode(.inline)
                }
                .presentationDetents([.medium, .large])
            }

            .alert("Enter URL", isPresented: $showingUrlInput) {
                TextField("URL", text: $urlInput)
                    .autocorrectionDisabled()
                Button("OK") {
                    if let url = URL(string: urlInput), UIApplication.shared.canOpenURL(url) {
                        icon = .image(url: url.absoluteString)
                    } else {
                        // Handle invalid URL
                        print("Invalid URL entered")
                    }
                }
                Button("Cancel", role: .cancel) {}.accentColor(.blue)
            } message: {
                Text("Please enter a valid URL")
            }
        }
    }

    private func selectEmoji(_ emoji: String) {
        icon = .emoji(value: emoji)
        showingEmojiPicker = false
    }

    private func selectImageUrl(_ url: String) {
        icon = .image(url: url)
        showingUrlInput = false
    }

    @MainActor private func saveCategory() {
        showNameError = name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
        let hasError = showNameError

        if hasError {
            return
        }

        let category = modelContext.createCategory(icon: icon, name: name)
        dismiss()
        onComplete(category)
    }


}

#Preview {
    CreateCategoryView() { category in

    }
}
