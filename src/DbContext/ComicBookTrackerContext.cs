using System;
using Microsoft.EntityFrameworkCore;
using ComicBookTracker.Models;

namespace ComicBookTracker
{
    public class ComicBookTrackerContext : DbContext
    {
        public ComicBookTrackerContext(DbContextOptions<ComicBookTrackerContext> options)
            : base(options)
        {
        }
        public DbSet<Issue> Issues { get; set; }
        public DbSet<Series> Series { get; set; }
        public DbSet<Publisher> Publishers { get; set; }
        public DbSet<Tag> Tags { get; set; }
        public DbSet<Author> Authors { get; set; }
        public DbSet<Trade> Trades { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            foreach (var entityType in modelBuilder.Model.GetEntityTypes())
            {
                foreach (var skipNavigation in entityType.GetSkipNavigations())
                {
                    Console.WriteLine(entityType.DisplayName() + "." + skipNavigation.Name);
                }
            }

            modelBuilder.Entity<Issue>()
                .HasMany(i => i.Tags)
                .WithMany(t => t.Issues)
                .UsingEntity<IssueTag>(
                    j => j.HasOne(it => it.Tag)
                        .WithMany(t => t.IssueTags)
                        .HasForeignKey(it => it.TagId),
                    j => j.HasOne(it => it.Issue)
                        .WithMany(i => i.IssueTags)
                        .HasForeignKey(it => it.IssueId),
                    j => j.HasKey(it => new { it.TagId, it.IssueId })
                );

            modelBuilder.Entity<Series>()
                .HasMany(s => s.Tags)
                .WithMany(t => t.Series)
                .UsingEntity<SeriesTag>(
                    j => j.HasOne(st => st.Tag)
                        .WithMany(t => t.SeriesTags)
                        .HasForeignKey(st => st.TagId),
                    j => j.HasOne(st => st.Series)
                        .WithMany(s => s.SeriesTags)
                        .HasForeignKey(st => st.SeriesId),
                    j => j.HasKey(st => new { st.TagId, st.SeriesId })
                );


            modelBuilder.Entity<Tag>()
                .HasMany(t => t.Issues)
                .WithMany(i => i.Tags)
                .UsingEntity<IssueTag>(
                    j => j.HasOne(it => it.Issue)
                        .WithMany(t => t.IssueTags)
                        .HasForeignKey(it => it.IssueId),
                    j => j.HasOne(it => it.Tag)
                        .WithMany(i => i.IssueTags)
                        .HasForeignKey(it => it.TagId),
                    j => j.HasKey(it => new { it.TagId, it.IssueId })
                );

            modelBuilder.Entity<Tag>()
                .HasMany(t => t.Series)
                .WithMany(s => s.Tags)
                .UsingEntity<SeriesTag>(
                    j => j.HasOne(st => st.Series)
                        .WithMany(t => t.SeriesTags)
                        .HasForeignKey(st => st.SeriesId),
                    j => j.HasOne(st => st.Tag)
                        .WithMany(s => s.SeriesTags)
                        .HasForeignKey(st => st.TagId),
                    j => j.HasKey(st => new { st.TagId, st.SeriesId})
                );



        }

    }
}
