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
                .accessibilityHidden(true)

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
    @Environment(\.requestReview) private var requestReview
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @AccessibilityFocusState private var isAddButtonFocused: Bool

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
                                        .accessibilityAddTraits(.isHeader)
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
                                        .accessibilityAddTraits(.isHeader)
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
                                                        deleteRejection(rejection)
                                                    } label: {
                                                        Image(systemName: "trash")
                                                            .foregroundColor(.white)
                                                    }
                                                    .accessibilityLabel("Delete")
                                                    .contentShape(Rectangle())
                                                    .frame(width: 60)
                                                    .frame(maxHeight: .infinity)
                                                    .background(Color.red) // <=== Look here
                                                }
                                            } action: { // <= action for full swiping
                                                deleteRejection(rejection)
                                            }
                                            .cornerRadius(10)
                                            .contextMenu {
                                                Button(role: .destructive) {
                                                    deleteRejection(rejection)
                                                } label: {
                                                    Label("Delete", systemImage: "trash")
                                                }
                                            }
                                            .accessibilityElement(children: .combine)
                                            .accessibilityAction(named: "Delete") {
                                                deleteRejection(rejection)
                                            }
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
            }
            .toolbar {
                ToolbarItem(placement: .automatic) {
                    Button {
                        showingAddRejection = true
                    } label: {
                        Image(systemName: "plus")
                    }
                    .accessibilityLabel("Add rejection")
                    .accessibilityFocused($isAddButtonFocused)
                }
            }
            .navigationTitle("Rejections")
            .sheet(isPresented: $showingAddRejection, onDismiss: {
                if newRejection == nil { isAddButtonFocused = true }
            }) {
                CreateRejectionView { rejection in
                    showingAddRejection = false
                    newRejection = rejection
                }
                onClose: {
                    showingAddRejection = false
                }
            }
            .sheet(item: $newRejection, onDismiss: {
                isAddButtonFocused = true
            }) { rejection in
                ShareView(rejection: rejection) {
                    newRejection = nil
                }
                .onDisappear {
                    // Fire the milestone review prompt on DISMISS of the
                    // celebratory share screen, not on open. The gate makes this
                    // fire exactly once, at the fifth logged rejection, with a
                    // 14-day cooldown shared with the manual "Rate This App" row.
                    requestReviewIfMilestoneReached()
                }
            }
        }
    }

    @MainActor
    private func deleteRejection(_ rejection: Rejection) {
        if reduceMotion {
            modelContext.deleteRejection(rejection)
        } else {
            withAnimation {
                modelContext.deleteRejection(rejection)
            }
        }
    }

    @MainActor
    private func requestReviewIfMilestoneReached() {
        guard ReviewPrompt.shouldRequest(
            for: .loggedRejection(count: rejections.count)
        ) else {
            return
        }

        // Let the share sheet finish dismissing before the system review sheet
        // presents over the Rejections tab.
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
            requestReview()
            ReviewPrompt.markMilestoneFired()
        }
    }
}

#Preview {
    ParraAppPreview {
        RejectionsTab()
    }
}
