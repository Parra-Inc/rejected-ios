//
//  TipJarCell.swift
//  Rejected
//
//  Created by Mick MacCallum on 10/24/24.
//

import Parra
import SwiftUI

struct TipJarCell: View {
    @State private var isTipJarPresented = false

    var body: some View {
        Button(action: {
            isTipJarPresented = true
        }) {
            Label(
                title: {
                    Text("Karma")
                        .foregroundStyle(Color.primary)
                },
                icon: {
                    Image(systemName: "heart")
                        .foregroundStyle(.tint)
                }
            )
        }
        .sheet(isPresented: $isTipJarPresented) {
            TipJarView(isPresented: $isTipJarPresented)
        }
    }
}
