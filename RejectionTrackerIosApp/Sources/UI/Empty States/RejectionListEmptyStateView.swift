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
                    .font(.system(size: 28, weight: .bold))

                Text("We're sorry you found us.\nAdd your rejection to get started!")
                    .font(.system(size: 18))
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

    var body: some View {
        Text("😭")
            .font(.system(size: 120))
            .rotationEffect(.degrees(wiggleAmount))
            .animation(
                Animation.easeInOut(duration: 0.5)
                    .repeatForever(autoreverses: true),
                value: wiggleAmount
            )
            .onAppear {
                wiggleAmount = 5
            }
    }
}

struct EmptyStateView_Previews: PreviewProvider {
    static var previews: some View {
        RejectionListEmptyStateView()
    }
}
