//
//  SampleTab.swift
//  Rejection Tracker iOS
//
//  Bootstrapped with ❤️ by Parra on 10/19/2024.
//  Copyright © 2024 Rejection Tracker. All rights reserved.
//

import Parra
import SwiftUI
import SwiftData
import SwipeActions

struct RejectionRow: View {
    let rejection: Rejection

    @Environment(\.parraTheme) var parraTheme

    var body: some View {
        HStack {
            IconView(icon: rejection.category?.decodedIcon())

            Text(rejection.title)
                .font(.headline)
                .fontWeight(.semibold)

            Spacer()
        }
        .padding(10)
        .background(parraTheme.palette.primaryBackground.toParraColor())
    }
}

struct RejectionsTab: View {
    @State private var newRejection: Rejection?
    @State private var showingAddRejection = false
    @State private var scrollInsetBottom: CGFloat = 44 // Estimate
    @Environment(\.parraTheme) var parraTheme
    @State var state: SwipeState = .untouched // <= HERE

    @Query(sort: \Rejection.createdAt, order: .reverse) var rejections: [Rejection]
    @Environment(\.modelContext) var modelContext

    var body: some View {
        NavigationView {
            ZStack {
                if rejections.isEmpty {
                    VStack {
                        Spacer()
                        RejectionListEmptyStateView()
                        Spacer()
                    }
                    .safeAreaInset(edge: .bottom, spacing: 0) {
                        // some bottom-sticked content, or just –
                        Spacer()
                            .frame(height: scrollInsetBottom)
                    }
                } else {
                    ScrollView {
                        VStack(spacing: 20) {
                            VStack {
                                HStack {
                                    Text("Stats")
                                        .font(.subheadline)
                                        .fontWeight(.semibold)
                                        .foregroundColor(.secondary)
                                    Spacer()
                                }
                                RejectionStatsView(rejections: rejections)
                            }

                            VStack {
                                HStack {
                                    Text("History")
                                        .font(.subheadline)
                                        .fontWeight(.semibold)
                                        .foregroundColor(.secondary)
                                    Spacer()
                                }
                                VStack(spacing: 6) {
                                    ForEach(rejections) { rejection in
                                        RejectionRow(rejection: rejection)
                                        .addFullSwipeAction(
                                            menu: .slided,
                                            swipeColor: .red, state: $state) { // <= Color is the same as last button in Trailing for full effect
                                                Leading {
                                                }
                                                Trailing {

                                                    Button {
                                                        withAnimation {
                                                            modelContext.deleteRejection(rejection)
                                                        }
                                                    } label: {
                                                        Image(systemName: "trash")
                                                            .foregroundColor(.white)
                                                    }
                                                    .contentShape(Rectangle())
                                                    .frame(width: 60)
                                                    .frame(maxHeight: .infinity)
                                                    .background(Color.red) // <=== Look here
                                                }
                                            } action: { // <= action for full swiping
                                                withAnimation {
                                                    modelContext.deleteRejection(rejection)
                                                }
                                            }
                                            .cornerRadius(10)
                                    }
                                }
                            }

                        }
                        .safeAreaPadding()
                    }
                    .safeAreaInset(edge: .bottom, spacing: 0) {
                        // some bottom-sticked content, or just –
                        Spacer()
                            .frame(height: scrollInsetBottom)
                    }
                }


                VStack {
                    Spacer()

                    LargeButton(title: "Add Rejection") {
                        showingAddRejection = true
                    }
                    .padding(.horizontal)
                    .padding(.vertical, 20)
                    .background {
                        GeometryReader { geometry in
                            LinearGradient(
                                gradient: Gradient(colors: [.white.opacity(0), .white, .white]),
                                startPoint: .top,
                                endPoint: .bottom
                            )
                            .task {
                                scrollInsetBottom = geometry.size.height
                            }
                        }
                    }
                }
            }
            .navigationTitle("Rejections")
            .sheet(isPresented: $showingAddRejection) {
                CreateRejectionView(isPresented: $showingAddRejection) { rejection in
                    showingAddRejection = false
                    newRejection = rejection
                }
            }
            .sheet(item: $newRejection) { rejection in
                ShareView(rejection: rejection) {
                    newRejection = nil
                }
            }
        }
    }
}

#Preview {
    ParraAppPreview {
        RejectionsTab()
    }
}
