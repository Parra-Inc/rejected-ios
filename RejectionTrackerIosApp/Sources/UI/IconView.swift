//
//  IconView.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import SwiftUI

struct IconView: View {
    enum Context {
        case add
    }

    enum Size: CGFloat, CaseIterable {
        case sm = 24
        case md = 36
        case lg = 48
        case xl = 64

        var padding: CGFloat {
            switch self {
            case .sm: return 4
            case .md: return 8
            case .lg: return 10
            case .xl: return 10
            }
        }

        var fontSize: CGFloat {
            switch self {
            case .sm: return 12
            case .md: return 16
            case .lg: return 20
            case .xl: return 36
            }
        }
    }


    @Environment(\.parraTheme) var parraTheme

    let icon: Icon?
    let context: Context?
    let size: Size

    init(icon: Icon?, size: Size = .md, context: Context? = nil) {
        self.icon = icon
        self.size = size
        self.context = context
    }

    var body: some View {
        Group {
            if let icon = icon {
                Group {
                    switch icon {
                    case .emoji(let value):
                        Text(value)
                            .font(.system(size: size.fontSize))
                    case .image(let url):
                        AsyncImage(url: URL(string: url)) { image in
                            image.resizable().scaledToFit()
                        } placeholder: {
                            ProgressView()
                        }
                    }
                }
                .frame(width: size.rawValue, height: size.rawValue)
                .background(Color.gray.opacity(0.1))

            } else {
                VStack {
                    if let context {
                        switch context {
                        case .add:
                            Image(systemName: "photo")
                                .font(.system(size: size.fontSize))
                                .foregroundColor(Color.gray.opacity(0.2))
                        }
                    }
                }
                .frame(width: size.rawValue, height: size.rawValue)
                .background(parraTheme.palette.primaryBackground.toParraColor())
            }
        }
        .cornerRadius(size.padding)
    }
}

#Preview {
    ForEach(IconView.Size.allCases, id: \.rawValue) { size in
        HStack(spacing: 8) {
            IconView(icon: nil, size: size)
            IconView(icon: nil, size: size, context: .add)
            IconView(icon: .emoji(value: "🍎"), size: size)
            IconView(
                icon: .image(url: "https://www.google.com/s2/favicons?sz=128&domain_url=https%3A%2F%2Fycombinator.com"),
                size: size
            )
        }
    }
}
