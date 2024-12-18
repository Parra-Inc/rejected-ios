//
//  EditProfileTextField.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import SwiftUI

struct EditProfileTextField: View {
    let name: String
    var value: Binding<String>

    var body: some View {
        HStack {
            Text(name)

            Spacer()

            TextField(
                name,
                text: value,
                prompt: Text(name)
            )
            .multilineTextAlignment(.trailing)
            .submitLabel(.done)
        }
    }
}
