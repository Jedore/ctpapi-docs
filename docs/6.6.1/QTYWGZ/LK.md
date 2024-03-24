<p>CTP交易系统基于安全和性能考虑，在诸多地方有流量控制，其中流量控制又分FTD报文流量控制、报单流量控制、查询流量控制等。而这些流量控制分布在各个不同的地方。此处将会给大家详细介绍。</p>
<span class="anchor" id="a2737a21-c539-49d7-8cad-ae0efb727a93"></span>
## 1.报单流控
<p>报单流控是指用户在本交易系统报单（<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>）、撤单（<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a>)时每秒内允许的最大笔数。</p>
<p>报单流控限制配置在CTP柜台端【程序化交易频繁报撤单管理】菜单。</p>
<p>如果超过这个限制API会通过<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPORDERACTION/">OnRspOrderAction</a>提示：“CTP:下单频率限制”。</p>
<span class="anchor" id="fc546bc4-744d-4519-bcf7-7a416d3d25ae"></span>
## 2.查询流控
<p>查询流控是指用户当前Session在做查询的时候每秒内允许的最大请求笔数。</p>
<p>查询流控配置在交易前置组件上，配置项为【QryFreq】。其中API内置了在途查询流控1笔。</p>
<p>自从穿透式监管版本以后，API在连接交易前置时，会去查询到前置的<code>查询流控设置</code>（该设置配置在front_se组件）。假设前置配置了2笔/秒，那么连接该前置的API每秒只能发起2笔查询请求。</p>
<p>但是要注意，不管怎么配置，<strong>API都内置了<code>在途流控</code>，在途查询流控为1笔</strong>。即，当前这笔查询请求发出后，在未收完所有的查询响应前，不能发起下一笔查询请求。</p>
<blockquote>
<p>在过去，查询流控是内置在API里，1笔每秒，在途1笔。</p>
</blockquote>
<p>如果超过交易前置配置的查询流控，则会触发<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPERROR/">OnRspError</a>，并提示：“CTP：查询未就绪，请稍后重试”</p>
<p>如果超过API内置的在途流控，则查询请求的返回值为-2，表示未处理请求超过许可数。</p>
<blockquote>
<p>所有ReqQuery开头查询函数不受流控限制，原因是此类函数都是通过交易核心处理的，不通过查询核心。</p>
</blockquote>
<span class="anchor" id="5bf07666-9aa0-4edf-afbf-858ff2ed920f"></span>
## 3.FTD报文流控
<p>FTD报文流控是指用户当前Session在提交API指令的时候每秒内允许的最大请求笔数。</p>
<p>FTD报文流控配置在交易前置组件上，配置项为【FTDMaxCommFlux】。</p>
<p>FTD报文流控是一种综合性的流控手段，API的所有接口在跟前置交互的时候都是使用FTD协议的报文进行通讯的，因此这就意味着，登录、查询、报单、撤单和报价等等所有请求都在FTD报文流控的限制范围内。</p>
<p>例如如果配置为6，可以简单理解为用户仅能调用6次API请求指令，包括登录、查询、报单撤单等等。</p>
<p>如果超过FTD报文流控，则超过的指令会被缓存到前置，直到下一秒发出。例如用户在一秒内报单10笔，则前6笔会立即发送给核心，而后4笔则会被缓存在前置，到下一秒才发出。因此对于用户程序端的感受就是后4笔报单延迟很大，实则是受到了流控。</p>
<p>注意，FTD报文流控不会有错误信息或错误返回。</p>
<span class="anchor" id="a27cc7c7-abef-48b8-a9ca-2600dfeff184"></span>
## 4.前置连接数流控
<p>前置连接数流控是指在本交易前置对同一IP每秒允许的最大API连接请求数。</p>
<p>前置连接数流控配置在交易前置组件上，配置项为【ConnectFreq】。如果不设置就表示不限制流控。</p>
<p>需要注意的是，API连接请求指的是API从init到<a href="../../HQJK/CTHOSTFTDCMDSPI/ONFRONTCONNECTED/">OnFrontConnected</a>的过程，跟登录无关。可以简单理解为一次init就是一个连接请求。</p>
<p>例如如果配置为20，则一秒内最多有20个session建立跟前置的连接。</p>
<p>如果超过前置连接数流控则会被主动断开连接，触发<a href="../../HQJK/CTHOSTFTDCMDSPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>。因此用户如果发现自己的程序一连接前置就被断开，则除了版本问题外，有可能是遇到了连接数流控。</p>
<blockquote>
<p>想要指定ip不受流控限制的话，可以通过在front_se的bin目录下面新建一个文件名为whiteiplist的文件，每个ip单独一行。</p>
</blockquote>
<span class="anchor" id="597853b6-25da-4c22-835a-68574a674d9f"></span>
## 5.同一用户最大允许在线会话数
<p>同一用户最大允许在线会话数是指同一个用户（UserID）在本交易系统中同时登录在线的最大允许会话数。</p>
<p>同一用户最大允许在线会话数配置在柜台或交易核心中。</p>
<p>注意，这个会话数针对的是本交易系统，而非单一前置。</p>
<p>如果超过同一用户最大允许在线会话，则会通过<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>返回“CTP:用户在线会话超出上限”的错误。</p>
<span class="anchor" id="86856f25-864e-4b6a-99aa-8645e431bd54"></span>
## 6.交易所API流控
<p>交易所API流控指通过交易所API发送报单等请求的每秒最大允许数。</p>
<p>交易所API流控的阈值设置在交易所端，由交易所API查询获取，该流控实际控制在交易所API端。</p>
<p>受到交易所流控后会触发<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>，报“CTP：交易所每秒发送请求数超过许可数”或者“CTP:交易所未处理请求超过许可数”。</p>
