/**
 * Next.js + Tailwind Component Generator
 */

class NextJSTailwindGenerator {
  constructor() {
    this.templates = {
      button: this.generateButton,
      input: this.generateInput,
      form: this.generateForm,
      card: this.generateCard,
      modal: this.generateModal,
      table: this.generateTable,
      navigation: this.generateNavigation,
      dashboard: this.generateDashboard,
      layout: this.generateLayout,
      page: this.generatePage
    };
  }

  /**
   * Generate component based on type and props
   */
  generateComponent(type, props = {}) {
    const generator = this.templates[type];
    if (!generator) {
      return this.generateGeneric(type, props);
    }
    return generator.call(this, props);
  }

  /**
   * Generate Button Component
   */
  generateButton(props) {
    const {
      name = 'CustomButton',
      variant = 'default',
      size = 'default',
      icon = null,
      loading = false,
      className = ''
    } = props;

    return `"use client"

import * as React from "react"
import { Button } from "@/components/ui/button"
${icon ? `import { ${icon} } from "lucide-react"` : ''}

interface ${name}Props {
  children: React.ReactNode
  onClick?: () => void
  disabled?: boolean
  loading?: boolean
  className?: string
}

export function ${name}({
  children,
  onClick,
  disabled = false,
  loading = false,
  className,
  ...props
}: ${name}Props) {
  return (
    <Button
      variant="${variant}"
      size="${size}"
      disabled={disabled || loading}
      onClick={onClick}
      className={\`\${loading ? 'opacity-50' : ''} \${className || ''}\`}
      {...props}
    >
      {loading ? (
        <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2" />
      ) : ${icon ? `<${icon} className="mr-2 h-4 w-4" />` : 'null'}}
      {children}
    </Button>
  )
}`;
  }

  /**
   * Generate Form Component
   */
  generateForm(props) {
    const {
      name = 'CustomForm',
      fields = [
        { name: 'email', type: 'email', label: 'Email', validation: 'email' },
        { name: 'message', type: 'textarea', label: 'Message', validation: 'min:10' }
      ]
    } = props;

    const fieldValidation = fields.map(field => {
      switch (field.validation) {
        case 'email':
          return `${field.name}: z.string().email("Please enter a valid email address")`;
        case 'required':
          return `${field.name}: z.string().min(1, "${field.label} is required")`;
        default:
          if (field.validation?.startsWith('min:')) {
            const min = field.validation.split(':')[1];
            return `${field.name}: z.string().min(${min}, "${field.label} must be at least ${min} characters")`;
          }
          return `${field.name}: z.string()`;
      }
    }).join(',\n  ');

    const fieldComponents = fields.map(field => `
          <FormField
            control={form.control}
            name="${field.name}"
            render={({ field }) => (
              <FormItem>
                <FormLabel>${field.label}</FormLabel>
                <FormControl>
                  ${field.type === 'textarea' 
                    ? `<Textarea placeholder="${field.placeholder || `Enter ${field.label.toLowerCase()}`}" {...field} />`
                    : `<Input type="${field.type}" placeholder="${field.placeholder || `Enter ${field.label.toLowerCase()}`}" {...field} />`
                  }
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />`).join('');

    return `"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import * as z from "zod"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { toast } from "sonner"

const formSchema = z.object({
  ${fieldValidation}
})

export function ${name}() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      ${fields.map(field => `${field.name}: ""`).join(',\n      ')}
    },
  })

  function onSubmit(values: z.infer<typeof formSchema>) {
    console.log(values)
    toast.success("Form submitted successfully!")
    form.reset()
  }

  return (
    <div className="mx-auto max-w-2xl space-y-6">
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
          ${fieldComponents}
          <Button type="submit" className="w-full">
            Submit
          </Button>
        </form>
      </Form>
    </div>
  )
}`;
  }

  /**
   * Generate Card Component
   */
  generateCard(props) {
    const {
      name = 'CustomCard',
      title = 'Card Title',
      description = 'Card description',
      withImage = false,
      withActions = false
    } = props;

    return `import * as React from "react"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
${withImage ? 'import Image from "next/image"' : ''}

interface ${name}Props {
  title?: string
  description?: string
  ${withImage ? 'imageSrc?: string\n  imageAlt?: string' : ''}
  children?: React.ReactNode
  className?: string
}

export function ${name}({
  title = "${title}",
  description = "${description}",
  ${withImage ? 'imageSrc,\n  imageAlt = "Card image",' : ''}
  children,
  className,
}: ${name}Props) {
  return (
    <Card className={className}>
      ${withImage ? `{imageSrc && (
        <div className="relative h-48 w-full overflow-hidden rounded-t-lg">
          <Image
            src={imageSrc}
            alt={imageAlt}
            fill
            className="object-cover"
          />
        </div>
      )}` : ''}
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent>
        {children}
      </CardContent>
      ${withActions ? `<CardFooter className="space-x-2">
        <Button variant="outline">Cancel</Button>
        <Button>Confirm</Button>
      </CardFooter>` : ''}
    </Card>
  )
}`;
  }

  /**
   * Generate Dashboard Page
   */
  generateDashboard(props) {
    const {
      name = 'Dashboard',
      widgets = ['stats', 'chart', 'table']
    } = props;

    return `"use client"

import * as React from "react"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import {
  BarChart3,
  TrendingUp,
  Users,
  DollarSign,
} from "lucide-react"

const stats = [
  {
    title: "Total Revenue",
    value: "$45,231.89",
    change: "+20.1% from last month",
    icon: DollarSign,
  },
  {
    title: "Active Users",
    value: "2,350",
    change: "+180.1% from last month",
    icon: Users,
  },
  {
    title: "Sales",
    value: "12,234",
    change: "+19% from last month",
    icon: BarChart3,
  },
  {
    title: "Growth",
    value: "573",
    change: "+201 since last hour",
    icon: TrendingUp,
  },
]

export default function ${name}() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold tracking-tight">Dashboard</h1>
        <Button>Download Report</Button>
      </div>
      
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat, index) => (
          <Card key={index}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">
                {stat.title}
              </CardTitle>
              <stat.icon className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stat.value}</div>
              <p className="text-xs text-muted-foreground">
                {stat.change}
              </p>
            </CardContent>
          </Card>
        ))}
      </div>
      
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
        <Card className="col-span-4">
          <CardHeader>
            <CardTitle>Overview</CardTitle>
          </CardHeader>
          <CardContent className="pl-2">
            <div className="h-[300px] flex items-center justify-center text-muted-foreground">
              Chart component would go here
            </div>
          </CardContent>
        </Card>
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Recent Activity</CardTitle>
            <CardDescription>
              You made 265 sales this month.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-8">
              {[1, 2, 3, 4].map((item) => (
                <div key={item} className="flex items-center">
                  <div className="h-9 w-9 rounded-full bg-primary/10 flex items-center justify-center">
                    <DollarSign className="h-4 w-4" />
                  </div>
                  <div className="ml-4 space-y-1">
                    <p className="text-sm font-medium leading-none">
                      Sale #{item}
                    </p>
                    <p className="text-sm text-muted-foreground">
                      $1,999.00
                    </p>
                  </div>
                  <div className="ml-auto font-medium">
                    +$1,999.00
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}`;
  }

  /**
   * Generate generic component
   */
  generateGeneric(type, props) {
    const { name = `Custom${type.charAt(0).toUpperCase() + type.slice(1)}` } = props;
    
    return `import * as React from "react"

interface ${name}Props {
  children?: React.ReactNode
  className?: string
}

export function ${name}({ children, className }: ${name}Props) {
  return (
    <div className={className}>
      {children || "Generated ${type} component"}
    </div>
  )
}`;
  }
}

// Export for use in claude-tools
module.exports = { NextJSTailwindGenerator };

// Usage examples:
/*
const generator = new NextJSTailwindGenerator();

// Generate a button
const buttonCode = generator.generateComponent('button', {
  name: 'SubmitButton',
  variant: 'default',
  icon: 'Send',
  loading: true
});

// Generate a form
const formCode = generator.generateComponent('form', {
  name: 'ContactForm',
  fields: [
    { name: 'email', type: 'email', label: 'Email', validation: 'email' },
    { name: 'message', type: 'textarea', label: 'Message', validation: 'min:10' }
  ]
});

// Generate a dashboard
const dashboardCode = generator.generateComponent('dashboard', {
  name: 'AnalyticsDashboard',
  widgets: ['stats', 'chart', 'table']
});
*/