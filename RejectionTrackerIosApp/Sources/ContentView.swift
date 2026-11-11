//
//  ContentView.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import RevenueHog
import SwiftUI

enum Tabs {
    case home
    case settings
    case search
}

struct ContentView: View {
    @State var selectedTab: Tabs = .home
    @State var searchString = ""
    @Environment(\.parraAuthState) private var parraAuthState

    var body: some View {
        TabView(selection: $selectedTab) {
            Tab("Rejections", systemImage: "xmark.circle", value: .home) {
                RejectionsTab()
            }

            Tab("Settings", systemImage: "gearshape", value: .settings) {
                SettingsTab()
            }

            Tab(value: .search, role: .search) {
                NavigationStack {
                    List {
                        Text("Search")
                    }
                    .navigationTitle("Search")
                    .searchable(text: $searchString)
                }
            }
        }
        .modifier(TabBarMinimizeOnScrollIfAvailable())
        // Link RevenueHog's anonymous id to the Parra account on login, and
        // forget it on logout so the next user starts fresh.
        .onChange(of: parraAuthState.user?.info.id, initial: true) { oldId, newId in
            if let newId {
                RevenueHog.identify(userId: newId)
            } else if oldId != nil {
                RevenueHog.reset()
            }
        }
//        .tabViewBottomAccessory {
//            LargeButton(title: "Add Rejection") {
//
//            }
//        }
//        .navigationTransition(.zoom)
    }
}

#Preview {
    ParraAppPreview(authState: .authenticatedPreview) {
        ContentView()
    }
}

/// iOS 26 minimizes the tab bar on scroll. On iOS 18 this modifier is a no-op.
private struct TabBarMinimizeOnScrollIfAvailable: ViewModifier {
    func body(content: Content) -> some View {
        if #available(iOS 26.0, *) {
            content.tabBarMinimizeBehavior(.onScrollDown)
        } else {
            content
        }
    }
}
