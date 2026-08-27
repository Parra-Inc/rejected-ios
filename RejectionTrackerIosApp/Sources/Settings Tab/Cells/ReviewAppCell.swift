//
//  ReviewAppCell.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import StoreKit
import SwiftUI

/// Settings "Rate This App" row. Asks the system for a review prompt for every
/// user, with no in-app rating collected first.
///
/// It used to open a custom 1-5 star sheet and forward only 5-star raters to the
/// store. That is review gating and it is a guideline 5.6.1 rejection.
///
/// Once this app has an App Store record, prefer opening
/// https://apps.apple.com/app/id<APP_ID>?action=write-review directly: a manual
/// tap deserves a composer that actually appears, and requestReview() is
/// silently throttled by the OS.
struct ReviewAppCell: View {
    @Environment(\.requestReview) private var requestReview

    var body: some View {
        Button {
            ReviewPrompt.markPrompted()
            requestReview()
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
    }
}

#Preview {
    ParraAppPreview(authState: .authenticatedPreview) {
        ReviewAppCell()
            .padding()
    }
}
