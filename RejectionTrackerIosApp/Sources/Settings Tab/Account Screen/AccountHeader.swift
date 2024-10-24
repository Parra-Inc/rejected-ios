//
//  AccountHeader.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI

struct AccountHeader: View {
    var body: some View {
        VStack {
            ParraProfilePhotoWell(
                size: CGSize(width: 100, height: 100)
            )
            .padding(.bottom, 6)

            IdentityLabels()
        }
        .padding()
        .frame(maxWidth: .infinity)
    }
}
