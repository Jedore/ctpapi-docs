<p>登出请求，对应响应OnRspUserLogout。暂不支持。</p>
<span class="anchor" id="44007127-e255-4a52-93cd-e73c6beb537e"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="91f290c7-f844-4517-a273-30348a542a43"></span>
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
<span class="anchor" id="ef3a4257-0c53-462e-bfd2-113969dafbfe"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d3719b75-16d7-4549-86d6-0346f6170496"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="4b31b7d2-4a1d-4614-b149-2c676fd2e4b0"></span>
## 5.FAQ
<p>无</p>
