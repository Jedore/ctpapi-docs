<p>请求查询投资单元</p>
<p>响应: OnRspQryInvestUnit</p>
<span class="anchor" id="02c14918-4388-415a-b447-0afd63e3414e"></span>
## 1.函数原型
<p>virtual int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) = 0;</p>
<span class="anchor" id="35c565b0-d807-4524-92f1-e1a4c231149f"></span>
## 2.参数
<p>pQryInvestUnit：查询投资单元</p>
<pre><code>struct CThostFtdcQryInvestUnitField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a9feb6cb-4d66-4eeb-a096-ed3ccecaba97"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a5244403-3e37-4077-9c59-ea576f407b0c"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a31eee40-3458-4728-86ef-ca8f1d8f6e51"></span>
## 5.FAQ
<p>无</p>
