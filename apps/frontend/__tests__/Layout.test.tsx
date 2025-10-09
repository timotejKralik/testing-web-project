

import { render, screen } from '@testing-library/react'
import Layout from '../components/Layout'

// Mock the child components that Layout uses
jest.mock('../components/navigation/Navigation', () => {
  return function MockNavigation() {
    return <div data-testid="mock-navigation">Navigation</div>
  }
})

jest.mock('../components/footer/Footer', () => {
  return function MockFooter() {
    return <div data-testid="mock-footer">Footer</div>
  }
})

// Mock the Alert component
jest.mock('../components/navigation/Alert', () => {
  return function MockAlert() {
    return <div data-testid="mock-alert">Alert Message</div>
  }
})

describe('Layout Component', () => {
  it('renders all layout components correctly', () => {
    render(
      <Layout>
        <div>Test Content</div>
      </Layout>
    )
    
    // Check if navigation is rendered
    expect(screen.getByTestId('mock-navigation')).toBeInTheDocument()
    
    // Check if footer is rendered
    expect(screen.getByTestId('mock-footer')).toBeInTheDocument()
    
    // Check if alert is rendered
    expect(screen.getByTestId('mock-alert')).toBeInTheDocument()
    
    // Check if children content is rendered
    expect(screen.getByText('Test Content')).toBeInTheDocument()
  })

  it('applies correct layout structure', () => {
    render(
      <Layout>
        <div>Test Content</div>
      </Layout>
    )
    
    // Get the main layout container
    const mainContainer = screen.getByRole('main')
    
    // Check if the layout structure is correct
    expect(mainContainer).toBeInTheDocument()
    expect(mainContainer).toContainElement(screen.getByText('Test Content'))
  })

  it('handles SEO metadata correctly', () => {
    const seoData = {
      title: 'Test Page',
      description: 'Test description',
      keywords: 'test, page, keywords'
    }
    
    render(
      <Layout seo={seoData}>
        <div>Test Content</div>
      </Layout>
    )
    
    // Check if SEO title is set
    expect(document.title).toBe('Test Page')
    
    // Check if meta description is set
    const metaDescription = document.querySelector('meta[name="description"]')
    expect(metaDescription).toHaveAttribute('content', 'Test description')
    
    // Check if meta keywords are set
    const metaKeywords = document.querySelector('meta[name="keywords"]')
    expect(metaKeywords).toHaveAttribute('content', 'test, page, keywords')
  })

  it('handles undefined SEO data gracefully', () => {
    render(
      <Layout>
        <div>Test Content</div>
      </Layout>
    )
    
    // Should not throw errors when SEO data is undefined
    expect(screen.getByText('Test Content')).toBeInTheDocument()
  })
})

