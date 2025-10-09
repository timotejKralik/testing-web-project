

import { render, screen } from '@testing-library/react'
import Footer from '../components/footer/Footer'

// Mock the GraphQL data that Footer component expects
const mockFooterData = {
  data: {
    footer: {
      data: {
        attributes: {
          links: [
            {
              id: 1,
              title: "About Us",
              url: "/about",
              isExternal: false
            },
            {
              id: 2,
              title: "Contact",
              url: "/contact",
              isExternal: false
            }
          ],
          socialMedia: [
            {
              id: 1,
              platform: "Twitter",
              url: "https://twitter.com/example"
            },
            {
              id: 2,
              platform: "LinkedIn",
              url: "https://linkedin.com/company/example"
            }
          ],
          copyright: "© 2025 Example Company. All rights reserved."
        }
      }
    }
  }
}

jest.mock('../generated/graphql', () => ({
  useFooterQuery: () => mockFooterData
}))

describe('Footer Component', () => {
  it('renders footer links correctly', () => {
    render(<Footer />)
    
    // Check if footer links are rendered
    expect(screen.getByText('About Us')).toBeInTheDocument()
    expect(screen.getByText('Contact')).toBeInTheDocument()
    
    // Check if links have correct href attributes
    const aboutLink = screen.getByText('About Us').closest('a')
    const contactLink = screen.getByText('Contact').closest('a')
    
    expect(aboutLink).toHaveAttribute('href', '/about')
    expect(contactLink).toHaveAttribute('href', '/contact')
  })

  it('renders social media links correctly', () => {
    render(<Footer />)
    
    // Check if social media links are rendered
    const twitterLink = screen.getByRole('link', { name: /twitter/i })
    const linkedinLink = screen.getByRole('link', { name: /linkedin/i })
    
    expect(twitterLink).toHaveAttribute('href', 'https://twitter.com/example')
    expect(linkedinLink).toHaveAttribute('href', 'https://linkedin.com/company/example')
  })

  it('displays copyright text', () => {
    render(<Footer />)
    
    // Check if copyright text is rendered
    expect(screen.getByText('© 2025 Example Company. All rights reserved.')).toBeInTheDocument()
  })

  it('handles external links correctly', () => {
    const mockDataWithExternalLink = {
      data: {
        footer: {
          data: {
            attributes: {
              ...mockFooterData.data.footer.data.attributes,
              links: [
                {
                  id: 3,
                  title: "External Link",
                  url: "https://example.com",
                  isExternal: true
                }
              ]
            }
          }
        }
      }
    }

    jest.spyOn(require('../generated/graphql'), 'useFooterQuery')
      .mockImplementation(() => mockDataWithExternalLink)

    render(<Footer />)
    
    // Check if external link has correct attributes
    const externalLink = screen.getByText('External Link').closest('a')
    expect(externalLink).toHaveAttribute('href', 'https://example.com')
    expect(externalLink).toHaveAttribute('target', '_blank')
    expect(externalLink).toHaveAttribute('rel', 'noopener noreferrer')
  })
})

