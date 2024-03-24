<p>查询最大报单数量响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYMAXORDERVOLUME/">ReqQryMaxOrderVolume</a>后，该方法被调用。</p>
<span class="anchor" id="25107093-2bad-4b82-8fe9-2ca4c5d27547"></span>
## 1.函数原型
<p>virtual void OnRspQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e27149c6-ea38-41e0-9ba2-6a1b94cad1e9"></span>
## 2.参数
<p>pQryMaxOrderVolume：查询最大报单数量</p>
<pre><code>struct CThostFtdcQryMaxOrderVolumeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///开平标志
    TThostFtdcOffsetFlagType OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///最大允许报单数量
    TThostFtdcVolumeType MaxVolume;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>MaxVolume：取值结果为，min（可开/可平，限价单最大下单量）；可开根据昨结算价计算得出。</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="adabda3f-08b3-4c42-a4c7-69e004cd85b5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="75578a2d-2893-4e81-9104-9b72f54d9741"></span>
## 4.FAQ
<p>无</p>
