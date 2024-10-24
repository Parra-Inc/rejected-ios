//
//  RejectionStatsView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI

struct RejectionStatsView: View {
    @Environment(\.parraTheme) var parraTheme
    let rejections: [Rejection]

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .top, spacing: 12) {
                totalRejectionsView
                Divider()
                lastRejectionView
            }
            .frame(maxWidth: .infinity)

            if !topCategories.isEmpty {
                Divider()
                topCategoriesView
            }
        }
        .padding()
        .background(parraTheme.palette.primaryBackground.toParraColor())
        .cornerRadius(10)
        .frame(maxWidth: .infinity)
    }

    private var totalRejectionsView: some View {
        HStack {
            VStack(alignment: .leading, spacing: 8) {
                Text("Total Rejections")
                    .font(.subheadline)
                    .fontWeight(.semibold)
                    .foregroundColor(.secondary)
                Text("\(rejections.count)")
                    .font(.headline)
            }

            Spacer()
        }
    }

    private var lastRejectionView: some View {
        HStack {
            VStack(alignment: .leading, spacing: 8) {
                Text("Last Rejection")
                    .font(.subheadline)
                    .fontWeight(.semibold)
                    .foregroundColor(.secondary)
                Text(formattedLastRejectionTime)
                    .font(.headline)
            }

            Spacer()
        }
    }

    private var topCategoriesView: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Top Categories")
                .font(.subheadline)
                .fontWeight(.semibold)
                .foregroundColor(.secondary)

            LazyVGrid(columns: [
                GridItem(.flexible()),
                GridItem(.flexible()),
                GridItem(.flexible())
            ], spacing: 6) {
                ForEach(topCategories, id: \.category.id) { categoryStats in
                    HStack {
                        IconView(icon: categoryStats.category.decodedIcon())

                        Text("\(categoryStats.count)")
                            .font(.headline)
                            .fontWeight(.semibold)

                        Spacer()
                    }
                }
            }
        }
    }

    private var topCategories: [(category: Category, count: Int)] {
        let categoryCounts = Dictionary(grouping: rejections, by: { $0.category })
            .mapValues { $0.count }

        return categoryCounts.sorted { $0.value > $1.value }
            .prefix(3)
            .compactMap { (category: Category?, count: Int) -> (category: Category, count: Int)? in
                guard let category = category else {
                    return nil
                }

                return (category, count)
            }
    }

    private var formattedLastRejectionTime: String {
        guard let lastRejection = rejections.max(by: { $0.createdAt < $1.createdAt }) else {
            return "-"
        }

        let timeInterval = Date().timeIntervalSince(lastRejection.createdAt)
        let formatter = DateComponentsFormatter()
        formatter.unitsStyle = .full
        formatter.maximumUnitCount = 1

        if timeInterval < 60 {
            return "Just now"
        } else if timeInterval < 3600 {
            formatter.allowedUnits = [.minute]
        } else if timeInterval < 86400 {
            formatter.allowedUnits = [.hour]
        } else {
            formatter.allowedUnits = [.day]
        }

        guard let formatted = formatter.string(from: timeInterval)?.lowercased() else {
            return "-"
        }

        return "\(formatted) ago"
    }
}

struct RejectionStatsView_Previews: PreviewProvider {
    static var previews: some View {
        VStack(spacing: 20) {
            RejectionStatsView(rejections: [
//                Rejection(category: "Job", title: "", note: "Not enough experience"),
//                Rejection(category: "Job", title: "", note: "Position filled"),
//                Rejection(category: "Dating", title: "", note: "Not interested"),
//                Rejection(category: "Project", title: "", note: "Budget constraints"),
//                Rejection(category: "Job", title: "", note: "Skills mismatch")
            ])

            RejectionStatsView(rejections: [])
        }
        .padding()
        .previewLayout(.sizeThatFits)
    }
}
