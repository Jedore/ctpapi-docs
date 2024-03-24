<p>请求查询二级代理操作员银期权限</p>
<p>响应: OnRspQrySecAgentACIDMap</p>
<span class="anchor" id="a8cf4fe9-3b9e-4721-b697-9e6a735fb847"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) = 0;</p>
<span class="anchor" id="abd39154-053b-4538-91a1-4ab14ed41252"></span>
## 2.参数
<p>pQrySecAgentACIDMap：二级代理操作员银期权限查询</p>
<pre><code>struct CThostFtdcQrySecAgentACIDMapField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///资金账户
    TThostFtdcAccountIDType AccountID;
    ///币种
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="83b8414b-7ffc-4d03-9d7a-a31057781abe"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b0811e44-6e1c-41a9-a5b3-d00902828ece"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2ed9d21a-aee1-4d1f-b938-aa142d90f3c9"></span>
## 5.FAQ
<p>无</p>
