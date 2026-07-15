//
//  ReviewAppCell.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI

/// Settings "Rate This App" row. Opens a custom 1-5 star sheet instead of
/// deep-linking straight to the App Store write-review page. Five stars fires the
/// system review prompt; one to four stars routes to the private feedback form.
struct ReviewAppCell: View {
    @State private var isRatingSheetPresented = false

    var body: some View {
        Button {
            isRatingSheetPresented = true
        } label: {
            HStack {
                Label(
                    title: {
                        Text("Rate This App")
                            .foregroundStyle(Color.primary)
                    },
                    icon: {
                        Image(systemName: "star")
                            .foregroundStyle(.tint)
                    }
                )

                Spacer()

                Image(systemName: "chevron.right")
                    .font(.footnote.weight(.semibold))
                    .foregroundStyle(.tertiary)
            }
        }
        .buttonStyle(.plain)
        .sheet(isPresented: $isRatingSheetPresented) {
            RatingPromptSheet()
        }
    }
}

#Preview {
    ParraAppPreview(authState: .authenticatedPreview) {
        ReviewAppCell()
            .padding()
    }
}
