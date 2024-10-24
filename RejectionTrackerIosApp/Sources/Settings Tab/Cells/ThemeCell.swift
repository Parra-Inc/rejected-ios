//
//  ThemeCell.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI

struct ThemeCell: View {
    @Environment(\.parraPreferredAppearance) private var appearance

    var body: some View {
        Picker(
            selection: appearance,
            content: {
                ForEach(ParraAppearance.allCases) { option in
                    Text(option.description).tag(option)
                }
            },
            label: {
                Label(
                    title: { Text("Theme") },
                    icon: { Image(systemName: "paintbrush") }
                )
            }
        )
    }
}

#Preview {
    ParraAppPreview {
        ThemeCell()
    }
}
