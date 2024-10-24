//
//  FormControl.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI

struct FormControl<Content: View>: View {
    let title: String?
    let error: String?
    let content: () -> Content
    let captionHeight = UIFont.preferredFont(forTextStyle: .caption1).lineHeight

    init(title: String? = nil, error: String? = nil, @ViewBuilder content: @escaping () -> Content) {
        self.title = title
        self.error = error
        self.content = content
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            if let title = title {
                Text(title)
                    .font(.subheadline)
                    .foregroundColor(Color.gray.opacity(0.8))
            }

            content()

            VStack {
                if let error = error {
                    Text(error)
                        .font(.caption)
                        .foregroundColor(.red)
                        .padding(.leading, 6)
                }
            }
            .frame(minHeight: captionHeight)
        }
    }
}

#Preview {
    FormControl(title: "Title", error: "Title is required") {

    }
}
