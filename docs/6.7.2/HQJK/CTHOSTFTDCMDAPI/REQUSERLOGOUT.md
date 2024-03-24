<p>登出请求，对应响应<a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>。暂不支持。</p>
<span class="anchor" id="be84baba-90b2-42de-ad6e-e44bb04ebf05"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="65b9bfd6-0ab1-4464-8874-9b1059e12ab7"></span>
## 2.参数
<p>pUserLogout：用户登出请求</p>
<pre><code>struct CThostFtdcUserLogoutField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="8e9eeb07-b610-4875-adae-5d3b58390f43"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b8b376df-5300-4128-8bda-d92896e6e07e"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="69d23457-3f35-48d3-8ba0-4f97a07ce9f2"></span>
## 5.FAQ
<p>无</p>
