//
//  RejectionListEmptyStateView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI

struct RejectionListEmptyStateView: View {
    @Environment(\.parraTheme) var parraTheme

    var body: some View {
        VStack() {
            LargeAnimatedEmojiView()

            VStack(spacing: 8) {
                Text("Oh no!")
                    .font(.title.bold())
                    .accessibilityAddTraits(.isHeader)

                Text("We're sorry you found us.\nAdd your rejection to get started!")
                    .font(.body)
                    .multilineTextAlignment(.center)
                    .foregroundColor(.secondary)
            }
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct LargeAnimatedEmojiView: View {
    @State private var wiggleAmount = 0.0
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @ScaledMetric(relativeTo: .largeTitle) private var emojiSize: CGFloat = 120

    var body: some View {
        Text("😭")
            .font(.system(size: emojiSize))
            .rotationEffect(.degrees(wiggleAmount))
            .animation(
                Animation.easeInOut(duration: 0.5)
                    .repeatForever(autoreverses: true),
                value: wiggleAmount
            )
            .onAppear {
                if !reduceMotion {
                    wiggleAmount = 5
                }
            }
            .accessibilityHidden(true)
    }
}

struct EmptyStateView_Previews: PreviewProvider {
    static var previews: some View {
        RejectionListEmptyStateView()
    }
}
