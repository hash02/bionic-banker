import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.string(),
    tags: z.array(z.string()).default([]),
    readTime: z.string().default('5 min'),
    featured: z.boolean().default(false),
    image: z.string().optional(),
    category: z.string().default('Tech'),
  }),
});

export const collections = { blog };
