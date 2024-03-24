<p>查询最大报单数量响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYMAXORDERVOLUME/">ReqQryMaxOrderVolume</a>后，该方法被调用。</p>
<span class="anchor" id="e4c2f213-e1c7-49fc-85e9-4d5a0056fec6"></span>
## 1.函数原型
<p>virtual void OnRspQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="11fb7899-8034-4387-a779-682903b21be2"></span>
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
<span class="anchor" id="8bbd82a7-989d-49c4-b76b-7b5f093f7948"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ec1ec4b2-97cd-4001-b03d-4ab1b960bbb3"></span>
## 4.FAQ
<p>无</p>
