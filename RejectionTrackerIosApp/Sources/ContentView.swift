//
//  ContentView.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            RejectionsTab()
                .tabItem {
                    Label("Rejections", systemImage: "xmark.circle")
                }
                .tag(1)

            SettingsTab()
                .tabItem {
                    Label("Settings", systemImage: "gearshape")
                }
        }
    }
}

#Preview {
    ParraAppPreview(authState: .authenticatedPreview) {
        ContentView()
    }
}
