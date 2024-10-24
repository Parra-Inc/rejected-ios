//
//  Icon.swift
//  RejectionTrackerIosApp
//
//  Created by Ian MacCallum on 10/19/24.
//

import Foundation

enum Icon: Codable {
    case emoji(value: String)
    case image(url: String)
}

