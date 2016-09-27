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

package org.glyptodon.guacamole.auth.jdbc;

import org.glyptodon.guacamole.auth.jdbc.user.UserContext;
import org.glyptodon.guacamole.auth.jdbc.connectiongroup.RootConnectionGroup;
import org.glyptodon.guacamole.auth.jdbc.connectiongroup.ModeledConnectionGroup;
import org.glyptodon.guacamole.auth.jdbc.connectiongroup.ConnectionGroupDirectory;
import org.glyptodon.guacamole.auth.jdbc.connection.ConnectionDirectory;
import org.glyptodon.guacamole.auth.jdbc.connection.ModeledGuacamoleConfiguration;
import org.glyptodon.guacamole.auth.jdbc.connection.ModeledConnection;
import org.glyptodon.guacamole.auth.jdbc.permission.SystemPermissionSet;
import org.glyptodon.guacamole.auth.jdbc.user.ModeledUser;
import org.glyptodon.guacamole.auth.jdbc.user.UserDirectory;
import org.glyptodon.guacamole.auth.jdbc.connectiongroup.ConnectionGroupMapper;
import org.glyptodon.guacamole.auth.jdbc.connection.ConnectionMapper;
import org.glyptodon.guacamole.auth.jdbc.connection.ConnectionRecordMapper;
import org.glyptodon.guacamole.auth.jdbc.connection.ParameterMapper;
import org.glyptodon.guacamole.auth.jdbc.permission.SystemPermissionMapper;
import org.glyptodon.guacamole.auth.jdbc.user.UserMapper;
import org.glyptodon.guacamole.auth.jdbc.connectiongroup.ConnectionGroupService;
import org.glyptodon.guacamole.auth.jdbc.connection.ConnectionService;
import org.glyptodon.guacamole.auth.jdbc.tunnel.GuacamoleTunnelService;
import org.glyptodon.guacamole.auth.jdbc.security.PasswordEncryptionService;
import org.glyptodon.guacamole.auth.jdbc.security.SHA256PasswordEncryptionService;
import org.glyptodon.guacamole.auth.jdbc.security.SaltService;
import org.glyptodon.guacamole.auth.jdbc.security.SecureRandomSaltService;
import org.glyptodon.guacamole.auth.jdbc.permission.SystemPermissionService;
import org.glyptodon.guacamole.auth.jdbc.user.UserService;
import org.apache.ibatis.transaction.jdbc.JdbcTransactionFactory;
import org.glyptodon.guacamole.auth.jdbc.permission.ConnectionGroupPermissionMapper;
import org.glyptodon.guacamole.auth.jdbc.permission.ConnectionGroupPermissionService;
import org.glyptodon.guacamole.auth.jdbc.permission.ConnectionGroupPermissionSet;
import org.glyptodon.guacamole.auth.jdbc.permission.ConnectionPermissionMapper;
import org.glyptodon.guacamole.auth.jdbc.permission.ConnectionPermissionService;
import org.glyptodon.guacamole.auth.jdbc.permission.ConnectionPermissionSet;
import org.glyptodon.guacamole.auth.jdbc.permission.UserPermissionMapper;
import org.glyptodon.guacamole.auth.jdbc.permission.UserPermissionService;
import org.glyptodon.guacamole.auth.jdbc.permission.UserPermissionSet;
import org.glyptodon.guacamole.auth.jdbc.activeconnection.ActiveConnectionDirectory;
import org.glyptodon.guacamole.auth.jdbc.activeconnection.ActiveConnectionPermissionService;
import org.glyptodon.guacamole.auth.jdbc.activeconnection.ActiveConnectionPermissionSet;
import org.glyptodon.guacamole.auth.jdbc.activeconnection.ActiveConnectionService;
import org.glyptodon.guacamole.auth.jdbc.activeconnection.TrackedActiveConnection;
import org.glyptodon.guacamole.auth.jdbc.tunnel.RestrictedGuacamoleTunnelService;
import org.glyptodon.guacamole.net.auth.AuthenticationProvider;
import org.mybatis.guice.MyBatisModule;
import org.mybatis.guice.datasource.builtin.PooledDataSourceProvider;

/**
 * Guice module which configures the injections used by the JDBC authentication
 * provider base. This module MUST be included in the Guice injector, or
 * authentication providers based on JDBC will not function.
 *
 * @author Michael Jumper
 * @author James Muehlner
 */
public class JDBCAuthenticationProviderModule extends MyBatisModule {

    /**
     * The environment of the Guacamole server.
     */
    private final JDBCEnvironment environment;

    /**
     * The AuthenticationProvider which is using this module to configure
     * injection.
     */
    private final AuthenticationProvider authProvider;

    /**
     * Creates a new JDBC authentication provider module that configures the
     * various injected base classes using the given environment, and provides
     * connections using the given socket service.
     *
     * @param authProvider
     *     The AuthenticationProvider which is using this module to configure
     *     injection.
     *
     * @param environment
     *     The environment to use to configure injected classes.
     */
    public JDBCAuthenticationProviderModule(AuthenticationProvider authProvider,
            JDBCEnvironment environment) {
        this.authProvider = authProvider;
        this.environment = environment;
    }

    @Override
    protected void initialize() {
        
        // Datasource
        bindDataSourceProviderType(PooledDataSourceProvider.class);
        
        // Transaction factory
        bindTransactionFactoryType(JdbcTransactionFactory.class);
        
        // Add MyBatis mappers
        addMapperClass(ConnectionMapper.class);
        addMapperClass(ConnectionGroupMapper.class);
        addMapperClass(ConnectionGroupPermissionMapper.class);
        addMapperClass(ConnectionPermissionMapper.class);
        addMapperClass(ConnectionRecordMapper.class);
        addMapperClass(ParameterMapper.class);
        addMapperClass(SystemPermissionMapper.class);
        addMapperClass(UserMapper.class);
        addMapperClass(UserPermissionMapper.class);
        
        // Bind core implementations of guacamole-ext classes
        bind(ActiveConnectionDirectory.class);
        bind(ActiveConnectionPermissionSet.class);
        bind(AuthenticationProvider.class).toInstance(authProvider);
        bind(JDBCEnvironment.class).toInstance(environment);
        bind(ConnectionDirectory.class);
        bind(ConnectionGroupDirectory.class);
        bind(ConnectionGroupPermissionSet.class);
        bind(ConnectionPermissionSet.class);
        bind(ModeledConnection.class);
        bind(ModeledConnectionGroup.class);
        bind(ModeledGuacamoleConfiguration.class);
        bind(ModeledUser.class);
        bind(RootConnectionGroup.class);
        bind(SystemPermissionSet.class);
        bind(TrackedActiveConnection.class);
        bind(UserContext.class);
        bind(UserDirectory.class);
        bind(UserPermissionSet.class);
        
        // Bind services
        bind(ActiveConnectionService.class);
        bind(ActiveConnectionPermissionService.class);
        bind(ConnectionGroupPermissionService.class);
        bind(ConnectionGroupService.class);
        bind(ConnectionPermissionService.class);
        bind(ConnectionService.class);
        bind(GuacamoleTunnelService.class).to(RestrictedGuacamoleTunnelService.class);
        bind(PasswordEncryptionService.class).to(SHA256PasswordEncryptionService.class);
        bind(SaltService.class).to(SecureRandomSaltService.class);
        bind(SystemPermissionService.class);
        bind(UserPermissionService.class);
        bind(UserService.class);
        
    }

}
