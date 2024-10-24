//
//  SettingsFooter.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI

struct SettingsFooter: View {
    @Environment(\.parraAppInfo) private var parraAppInfo

    @ViewBuilder 
    var body: some View {
        let version =
            "Version \(Parra.appBundleVersionShort()!) (\(Parra.appBundleVersion()!))"

        HStack(alignment: .center) {
            Text(version)
                .font(.footnote)
                .foregroundStyle(.gray)

            if !parraAppInfo.tenant.hideBranding {
                Divider()

                PoweredByParraButton()
            }
        }
        .padding(.vertical, 20)
        .frame(maxWidth: .infinity)
    }
}

#Preview {
    ParraAppPreview {
        SettingsFooter()
    }
}
