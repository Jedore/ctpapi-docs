<p>登出请求，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>。暂不支持。</p>
<span class="anchor" id="0f898750-11da-4fcc-98c5-f154504df528"></span>
## 1.函数原型
<p>virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="aee0d299-13ad-468f-b691-16f9241312fb"></span>
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
<span class="anchor" id="b4c0579c-6b04-4f5f-99e4-bd8235b609df"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c61357f2-9123-447f-aa6e-f64b8febf743"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="2d96a9a1-4412-4fcf-9aa2-6cced09eacb4"></span>
## 5.FAQ
<p>无</p>
