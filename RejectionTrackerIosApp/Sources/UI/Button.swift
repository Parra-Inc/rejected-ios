//
//  Button.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI

struct LargeButton: View {
    enum Style {
        case primary
        case secondary
    }

    @Environment(\.parraTheme) var parraTheme

    let title: String
    let style: Style
    let action: () -> Void

    private var backgroundColor: Color {
        switch style {
        case .primary:
            return parraTheme.palette.primary.toParraColor()
        case .secondary:
            return parraTheme.palette.secondary.toParraColor()
        }
    }

    init(title: String, style: Style = .primary, action: @escaping () -> Void) {
        self.title = title
        self.style = style
        self.action = action
    }

    var body: some View {
        Button(action: {
            action()
        }) {
            Text(title)
                .font(.headline)
                .foregroundColor(.white)
                .frame(maxWidth: .infinity)
                .padding()
                .background(backgroundColor)
                .cornerRadius(10)
        }
    }
}

#Preview {
    LargeButton(title: "Save") {

    }
}
