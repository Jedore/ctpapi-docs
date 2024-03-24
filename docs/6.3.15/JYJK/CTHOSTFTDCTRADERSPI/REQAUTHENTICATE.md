<p>客户端认证请求，对应响应OnRspAuthenticate。如果交易系统开启了强制终端认证，则必须认证通过后才能发起登陆；如果未开启，则不需要认证即可登陆，此时如果主动去认证，不管成功或失败，也不影响后续登陆。</p>
<span class="anchor" id="0aae2492-4f86-4054-b3fb-c65334e849b2"></span>
## 1.函数原型
<p>virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) = 0;</p>
<span class="anchor" id="3e1236e8-44b5-49ba-9975-217d05c59856"></span>
## 2.参数
<p>pReqAuthenticateField：客户端认证请求</p>
<pre><code>struct CThostFtdcReqAuthenticateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///认证码
    TThostFtdcAuthCodeType AuthCode;
    ///App代码
    TThostFtdcAppIDType AppID;
};
</code></pre>
<p>UserProductInfo：客户端的产品信息，如软件开发商、版本号等。</p>
<blockquote>
<p>例如：SFITTraderV100。该字段可以不填写。</p>
</blockquote>
<p>AuthCode：认证码需要向期货公司申请得到</p>
<p>AppID：<strong><font color="#FF0000">必填项</font></strong>，不然认证失败，如果没有则要向期货公司申请，申请的AppID必须遵循监控中心规范格式</p>
<p>UserID：<strong><font color="#FF0000">必填项</font></strong>，用户代码。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="680f392a-21ff-4faf-8c09-2b3298864839"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8ae6f35c-3249-4de2-84b7-e67ae217b002"></span>
## 4.调用示例
<pre><code>CThostFtdcReqAuthenticateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.UserProductInfo, "mytest");
strcpy_s(a.AuthCode, "MLX0LEA4L4UPUCBF"); 
strcpy_s(a.AppID, "mytest");
m_pUserApi-&gt;ReqAuthenticate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="7ca9d1d1-b55b-427a-a6a7-9e453d4c6583"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">每次重连都需要做一遍客户端认证吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>重新连接都需要重新认证一下。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">非穿透式版本，开通了强制认证，需要申请一个认证码的。穿透式版本，也需要一个穿透式的认证码。如果想同时开通非穿透式强制认证和穿透式认证，这样就要两个认证码；但API里是只需要一个认证码，那请问这种情况怎么解决？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>这种场景是不存在的，因为穿透式和非穿透式版本的api互不兼容，所以不存在用一个api去同时做新旧前置的认证。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">在使用“看穿式监管信息采集评测工具”时候，发现获取到的记录数和数据库中信息的条目数不匹配。这是为什么？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>数据库中的记录为乱码的话就不显示。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">采集信息库是否是线程安全的？能多个线程同时调用吗？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>不是线程安全的，不能同时调用。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
