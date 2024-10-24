//
//  ShareCell.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI

struct ShareCell: View {
    @Environment(\.parraAppInfo) private var parraAppInfo

    var body: some View {
        if let appStoreUrl = parraAppInfo.application.appStoreUrl {
            HStack {
                ShareLink(item: appStoreUrl, message: Text(Config.shareDescription)) {
                    Label(
                        title: {
                            Text("Share this App")
                        },
                        icon: {
                            Image(systemName: "square.and.arrow.up")
                                .foregroundStyle(.tint)
                        }
                    )
                }
                .foregroundStyle(Color.primary)

                Spacer()

                Image(systemName: "arrow.up.right")
                    .foregroundStyle(.gray)
            }
        }
    }
}

#Preview {
    ParraAppPreview {
        ShareCell()
    }
}
