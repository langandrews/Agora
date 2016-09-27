/*
 * Copyright (C) 2015 Glyptodon LLC
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

package org.glyptodon.guacamole.auth.jdbc.connection;

import java.util.Collection;
import java.util.List;
import org.apache.ibatis.annotations.Param;
import org.glyptodon.guacamole.auth.jdbc.user.UserModel;

/**
 * Mapper for connection record objects.
 *
 * @author Michael Jumper
 */
public interface ConnectionRecordMapper {

    /**
     * Returns a collection of all connection records associated with the
     * connection having the given identifier.
     *
     * @param identifier
     *     The identifier of the connection whose records are to be retrieved.
     *
     * @return
     *     A collection of all connection records associated with the
     *     connection having the given identifier. This collection will be
     *     empty if no such connection exists.
     */
    List<ConnectionRecordModel> select(@Param("identifier") String identifier);

    /**
     * Inserts the given connection record.
     *
     * @param record
     *     The connection record to insert.
     *
     * @return
     *     The number of rows inserted.
     */
    int insert(@Param("record") ConnectionRecordModel record);

    /**
     * Searches for up to <code>limit</code> connection records that contain
     * the given terms, sorted by the given predicates, regardless of whether
     * the data they are associated with is is readable by any particular user.
     * This should only be called on behalf of a system administrator. If
     * records are needed by a non-administrative user who must have explicit
     * read rights, use searchReadable() instead.
     *
     * @param terms
     *     The search terms that must match the returned records.
     *
     * @param sortPredicates
     *     A list of predicates to sort the returned records by, in order of
     *     priority.
     *
     * @param limit
     *     The maximum number of records that should be returned.
     *
     * @return
     *     The results of the search performed with the given parameters.
     */
    List<ConnectionRecordModel> search(@Param("terms") Collection<ConnectionRecordSearchTerm> terms,
            @Param("sortPredicates") List<ConnectionRecordSortPredicate> sortPredicates,
            @Param("limit") int limit);

    /**
     * Searches for up to <code>limit</code> connection records that contain
     * the given terms, sorted by the given predicates. Only records that are
     * associated with data explicitly readable by the given user will be
     * returned. If records are needed by a system administrator (who, by
     * definition, does not need explicit read rights), use search() instead.
     *
     * @param user
     *    The user whose permissions should determine whether a record is
     *    returned.
     *
     * @param terms
     *     The search terms that must match the returned records.
     *
     * @param sortPredicates
     *     A list of predicates to sort the returned records by, in order of
     *     priority.
     *
     * @param limit
     *     The maximum number of records that should be returned.
     *
     * @return
     *     The results of the search performed with the given parameters.
     */
    List<ConnectionRecordModel> searchReadable(@Param("user") UserModel user,
            @Param("terms") Collection<ConnectionRecordSearchTerm> terms,
            @Param("sortPredicates") List<ConnectionRecordSortPredicate> sortPredicates,
            @Param("limit") int limit);

}
