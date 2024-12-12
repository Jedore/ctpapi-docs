<p>CTP交易系统基于安全和性能考虑，在行情中新增登录和流控限制，分别对应的配置项和api回调中的表现各不相同。此处将会给大家详细介绍。</p>
<span class="anchor" id="c9e1c3ca-0c81-4cf7-9c98-bb50305f5d67"></span>
## 1.行情登录验证
<p>配置在行情前置组件上，配置项为</p>
<p class="comment">LoginVerify=yes</p>
<p>开启后登录行情前置时要求当前交易日UserID+IP 已成功登录过交易系统。开启此功能会影响部分客户端，需要改 造适配：先登录交易后登行情。 </p>
<p>API报错“CTP: 不合法的登录”</p>
<span class="anchor" id="3d2bc24c-823c-4430-abcc-cae753b173c8"></span>
## 2.单session登录频率限制
<p>配置在行情前置组件上，配置项为</p>
<p class="comment">LoginFreq=1</p>
<p>如上配置表示每个session每秒可以登录的频率为一秒一次，默认为该值</p>
<p>配置为0表示登录频率不限制</p>
<p>API报错“CTP: api login over limit freq”</p>
<span class="anchor" id="a6176ebc-40bf-4e17-84b7-74fa6d18dee6"></span>
## 3.给各个session发送缓存包限制
<p>配置在行情前置组件上，配置项为</p>
<p class="comment">SendingListSize</p>
<p>前置给每个session发送数据的缓存包上限。缓存包超出上限则主动断开会话。</p>
<p>该配置项如不设置，默认该值为10000。如设置，则实际请求包的缓存上限为max（10000，设置的值）</p>
<span class="anchor" id="70302098-a284-4986-b464-08a3137d7e6e"></span>
## 4.行情前置连接数流控
<p>前置连接数流控是指在本行情前置对同一IP每秒允许的最大API连接请求数。</p>
<p>前置连接数流控配置在行情前置组件上，配置项为【ConnectFreq】。如果不设置就表示不限制流控。</p>
<p>需要注意的是，API连接请求指的是API从init到<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>的过程，跟登录无关。可以简单理解为一次init就是一个连接请求。</p>
<p>例如如果配置为20，则一秒内最多有20个session建立跟前置的连接。</p>
<p>如果超过前置连接数流控则会被主动断开连接，触发<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>。因此用户如果发现自己的程序一连接前置就被断开，则除了版本问题外，有可能是遇到了连接数流控。</p>
<blockquote>
<p>想要指定ip不受流控限制的话，可以通过在front_md_se的bin目录下面新建一个文件名为whiteiplist的文件，每个ip单独一行。</p>
</blockquote>
<span class="anchor" id="4b376c39-071a-4949-99e3-99098fee2b71"></span>
## 5.行情前置IP最大session连接数限制、最大可订阅合约数限制
<p>ctp系统版本自6.7.2P6开始，行情前置新增配置项。</p>
<p>每个IP上活跃的session个数限制，默认为0不限制</p>
<p class="comment">MaxIPSession=10</p>
<p>每个session上订阅合约个数限制，默认为0不限制</p>
<p class="comment">MaxSubInstCnt=0</p>
<p>默认不配置，即不限制。</p>
<p>若超 MaxIPSession 限制后，会断开新建 session</p>
<p>若超 MaxSubInstCnt 限制后，会给 API 返回订阅失败，失败原因 6000，原因值“CTP:sub too many insts”</p>
<blockquote>
<p>想要指定ip不受以上限制，可以通过在front_md_se的bin目录下面新建一个文件名为whiteiplist的文件，每个ip单独一行。</p>
</blockquote>
