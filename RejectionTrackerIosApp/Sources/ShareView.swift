//
//  ShareView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import Parra
import SwiftUI

struct ShareView: View {
    @State private var showSmiley = false
    @State private var bounce = false
    @State private var isTipJarPresented = false

    @Environment(\.parraAppInfo) private var parraAppInfo

    let rejection: Rejection
    let onComplete: () -> Void

    var body: some View {
        VStack {
            Spacer()

            VStack(spacing: 12) {
                ZStack {
                    Text("😭")
                        .font(.system(size: 120))
                        .opacity(showSmiley ? 0 : 1)

                    Text("🤠")
                        .font(.system(size: 120))
                        .opacity(showSmiley ? 1 : 0)
                        .scaleEffect(bounce ? 1.2 : 1.0)
                }
                .animation(.easeInOut(duration: 1.5).delay(2), value: showSmiley)
                .animation(.interpolatingSpring(stiffness: 300, damping: 10).delay(3), value: bounce)

                Text("Now it's time to turn that frown upside down, get back out there and grind harder!")
                    .font(.headline)
                    .multilineTextAlignment(.center)
                    .frame(maxWidth: 240)
            }
            .padding()


            Spacer()

            Text("Remember: doing something nice for others when you're down is the best way to help you feel better :)")
                .font(.subheadline)
                .multilineTextAlignment(.center)
                .foregroundColor(.secondary)
                .padding()

            HStack(spacing: 12) {
                if let appStoreUrl = parraAppInfo.application.appStoreUrl {

                    ShareLink(item: appStoreUrl, message: Text(Config.shareDescription)) {
                        Label(
                            title: {
                                Text("Share")
                            },
                            icon: {
                                Image(systemName: "square.and.arrow.up")
                                    .foregroundStyle(.tint)
                            }
                        )
                    }
                    .frame(maxWidth: .infinity)
                    .foregroundStyle(Color.primary)
                    .padding()
                    .background(Color.gray.opacity(0.2))
                    .foregroundColor(.primary)
                    .cornerRadius(10)
                }

                Button(action: {
                    isTipJarPresented = true
                }) {
                    HStack {
                        Image(systemName: "heart")
                            .foregroundStyle(.tint)

                        Text("Karma")
                    }
                    .frame(maxWidth: .infinity)
                }
                .buttonStyle(LightGrayButtonStyle())
                .sheet(isPresented: $isTipJarPresented) {
                    TipJarView(isPresented: $isTipJarPresented)
                }
            }
            .padding(.horizontal)
            .padding(.bottom, 16)

            VStack(alignment: .center) {
                PoweredByParraButton()
            }
            .safeAreaPadding(.bottom, 8)
        }
        .presentationDetents([.large])
        .presentationDragIndicator(.visible)
        .onAppear {
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                showSmiley = true
                DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
                    bounce = true
                }
            }
        }
    }
}

struct LightGrayButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(Color.gray.opacity(0.2))
            .foregroundColor(.primary)
            .cornerRadius(10)
            .scaleEffect(configuration.isPressed ? 0.95 : 1)
    }
}


#Preview {
    ShareView(rejection: .init(category: .init(icon: nil, name: "Collecte"), title: "Stanford", note: "Sad :(")) {

    }
}
