
import { render, screen } from '@testing-library/react'
import BlogPage from '../pages/blog/[slug]'

// Mock the GraphQL data that BlogPage component expects
const mockBlogData = {
  data: {
    blogs: {
      data: [{
        id: '1',
        attributes: {
          title: 'Test Blog Post',
          content: 'This is a test blog post content',
          slug: 'test-blog-post',
          publishedAt: '2025-10-09T12:00:00Z',
          writer: {
            data: {
              attributes: {
                name: 'John Doe',
                role: 'Author'
              }
            }
          },
          category: {
            data: {
              attributes: {
                name: 'Technology',
                slug: 'technology'
              }
            }
          }
        }
      }]
    }
  }
}

jest.mock('../generated/graphql', () => ({
  useBlogBySlugQuery: () => mockBlogData
}))

describe('Blog Page', () => {
  it('renders blog post content correctly', () => {
    render(<BlogPage slug="test-blog-post" />)
    
    // Check if blog title is rendered
    expect(screen.getByText('Test Blog Post')).toBeInTheDocument()
    
    // Check if blog content is rendered
    expect(screen.getByText('This is a test blog post content')).toBeInTheDocument()
    
    // Check if author information is rendered
    expect(screen.getByText('John Doe')).toBeInTheDocument()
    expect(screen.getByText('Author')).toBeInTheDocument()
    
    // Check if category is rendered
    expect(screen.getByText('Technology')).toBeInTheDocument()
  })

  it('displays formatted publication date', () => {
    render(<BlogPage slug="test-blog-post" />)
    
    // Check if the date is formatted and displayed
    const date = new Date('2025-10-09T12:00:00Z')
    const formattedDate = date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
    expect(screen.getByText(formattedDate)).toBeInTheDocument()
  })
})
