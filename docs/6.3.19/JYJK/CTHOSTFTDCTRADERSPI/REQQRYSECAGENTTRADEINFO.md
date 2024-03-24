<p>请求查询二级代理商信息</p>
<p>响应: OnRspQrySecAgentTradeInfo</p>
<span class="anchor" id="264bff3d-9de3-4016-af64-255f827d0e9d"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="5b7fb87a-8e81-4517-ab9d-755ea8889617"></span>
## 2.参数
<p>pQrySecAgentTradeInfo：查询二级代理商信息</p>
<pre><code>struct CThostFtdcQrySecAgentTradeInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///境外中介机构资金帐号
    TThostFtdcAccountIDType BrokerSecAgentID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3b72db4c-02cc-4bc6-bbe3-4026b1114ded"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4237c6e5-65a5-4bbb-bf9a-c7a5f058ab75"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ef890eeb-87f3-4bbd-8628-c7698d71d140"></span>
## 5.FAQ
<p>无</p>
