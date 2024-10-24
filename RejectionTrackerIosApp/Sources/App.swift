//
//  RejectionTrackerIosAppApp.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI
import SwiftData

class AppDelegate: ParraAppDelegate<ParraSceneDelegate> {
    override func application(
        _ application: UIApplication,
        supportedInterfaceOrientationsFor window: UIWindow?
    ) -> UIInterfaceOrientationMask {
        return .portrait
    }
}

@main
struct RejectionTrackerIosApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

    @AppStorage("db_seeded") private var seeded = false

    var body: some Scene {
        // Visit Parra's configuration docs to learn what options are available.
        // https://docs.parra.io/sdks/ios/configuration
        ParraApp(
            tenantId: "<PARRA_TENANT_ID>",
            applicationId: "<PARRA_APPLICATION_ID>",
            appDelegate: appDelegate,
            configuration: ParraConfiguration(
            theme: ParraTheme(
                lightPalette: ParraColorPalette(
                    primary: ParraColorSwatch(
                        primary: Color(red: 247 / 255.0, green: 67 / 255.0, blue: 84 / 255.0),
                        name: "Primary"
                    ),
                    secondary: ParraColorSwatch(
                        primary: Color.secondary,
                        name: "Secondary"
                    ),
                    primaryBackground: Color(red: 247 / 255.0, green: 247 / 255.0, blue: 247 / 255.0),
                    secondaryBackground: Color(UIColor.secondarySystemBackground),
                    primaryText: ParraColorSwatch(
                        primary: Color(red: 17 / 255.0, green: 24 / 255.0, blue: 39 / 255.0),
                        name: "Primary Text"
                    ),
                    secondaryText: ParraColorSwatch(
                        primary: Color(red: 60 / 255.0, green: 60 / 255.0, blue: 67 / 255.0),
                        name: "Secondary Text"
                    ),
                    primarySeparator: ParraColorSwatch(
                        primary: Color(red: 229 / 255.0, green: 231 / 255.0, blue: 235 / 255.0),
                        name: "Primary Separator"
                    ),
                    secondarySeparator: ParraColorSwatch(
                        primary: Color(red: 198 / 255.0, green: 198 / 255.0, blue: 198 / 255.0),
                        name: "Secondary Separator"
                    ),
                    error: ParraColorSwatch(
                        primary: Color(red: 225 / 255.0, green: 82 / 255.0, blue: 65 / 255.0),
                        name: "Error"
                    ),
                    warning: ParraColorSwatch(
                        primary: Color(red: 253 / 255.0, green: 169 / 255.0, blue: 66 / 255.0),
                        name: "Warning"
                    ),
                    info: ParraColorSwatch(
                        primary: Color(red: 38 / 255.0, green: 139 / 255.0, blue: 210 / 255.0),
                        name: "Info"
                    ),
                    success: ParraColorSwatch(primary: .green, name: "Success")
                )
            )
            )

        ) {
            WindowGroup {
                // Use the ParraOptionalAuthWindow if you don't support user sign-in
                // or don't require that users be logged in to use your app. Use
                // ParraRequiredAuthWindow if signing in is required.
                ParraOptionalAuthWindow {
                    ContentView()
                }
            }
        }
        .modelContainer(for: [Rejection.self, Category.self]) { result in
            do {
                if seeded {
                    return
                }

                let container = try result.get()

                let categories: [Category] = [
                    Category(icon: .emoji(value: "🍎"), name: "College"),
                    Category(icon: .emoji(value: "💔"), name: "Romantic"),
                    Category(icon: .emoji(value: "💼"), name: "Job"),
                    Category(
                        icon: .image(url: "https://www.google.com/s2/favicons?sz=64&domain_url=https%3A%2F%2Fycombinator.com"),
                        name: "YCombinator"
                    ),
                    Category(icon: .emoji(value: "💰"), name: "Investor"),
                ]

                for category in categories {
                    container.mainContext.insert(category)
                }

                seeded = true
            } catch {
                print("Failed to pre-seed database.")
            }
        }
    }
}
