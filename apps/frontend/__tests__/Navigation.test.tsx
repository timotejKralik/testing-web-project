
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Navigation from '../components/navigation/Navigation'

// Mock the GraphQL data that Navigation component expects
const mockNavigationData = {
  data: {
    navigation: {
      data: {
        attributes: {
          links: [
            {
              id: 1,
              title: "Home",
              url: "/",
              isExternal: false,
              children: []
            },
            {
              id: 2,
              title: "Blog",
              url: "/blog",
              isExternal: false,
              children: []
            }
          ]
        }
      }
    }
  }
}

jest.mock('../generated/graphql', () => ({
  useNavigationQuery: () => mockNavigationData
}))

describe('Navigation Component', () => {
  it('renders navigation links correctly', () => {
    render(<Navigation />)
    
    // Check if main navigation links are rendered
    expect(screen.getByText('Home')).toBeInTheDocument()
    expect(screen.getByText('Blog')).toBeInTheDocument()
  })

  it('handles mobile menu toggle correctly', async () => {
    render(<Navigation />)
    
    // Find and click the mobile menu button
    const menuButton = screen.getByRole('button', { name: /menu/i })
    await userEvent.click(menuButton)
    
    // Check if mobile menu is visible
    const mobileMenu = screen.getByRole('dialog')
    expect(mobileMenu).toBeInTheDocument()
    
    // Close menu
    const closeButton = screen.getByRole('button', { name: /close/i })
    await userEvent.click(closeButton)
    
    // Check if mobile menu is closed
    expect(mobileMenu).not.toBeVisible()
  })
})
