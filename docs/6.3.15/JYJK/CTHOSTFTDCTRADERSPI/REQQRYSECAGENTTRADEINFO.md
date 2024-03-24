<p>请求查询二级代理商信息</p>
<p>响应: OnRspQrySecAgentTradeInfo</p>
<span class="anchor" id="11d10d05-37eb-426a-8965-9e2be9d2f1bb"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentTradeInfo(CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID) = 0;</p>
<span class="anchor" id="742e8890-6d8c-4311-ba0d-4b211735a6aa"></span>
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
<span class="anchor" id="95efc56b-b7cd-4db1-b4db-4873e3419827"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d53e06ac-d9bd-4014-9e25-a970bf840479"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="92180ae2-213f-49f4-af20-cc57c50c4ef1"></span>
## 5.FAQ
<p>无</p>
