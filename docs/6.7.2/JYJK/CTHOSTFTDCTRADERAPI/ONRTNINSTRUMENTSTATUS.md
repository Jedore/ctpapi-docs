<p>合约交易状态通知，主动推送。公有流回报。</p>
<p>各交易所的合约状态变化详见<a href="../../../QTYWGZ/HYZTBHSM/">合约状态变化说明</a>。</p>
<span class="anchor" id="dfadb95d-5068-4200-b961-9ad4b8a1cd93"></span>
## 1.函数原型
<p>virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {};</p>
<span class="anchor" id="d1387c2c-822a-4b5f-8afd-9beeb9d93a72"></span>
## 2.参数
<p>pInstrumentStatus：合约状态</p>
<pre><code>struct CThostFtdcInstrumentStatusField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve1;
    ///结算组代码
    TThostFtdcSettlementGroupIDType SettlementGroupID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve2;
    ///合约交易状态
    TThostFtdcInstrumentStatusType  InstrumentStatus;
    ///交易阶段编号
    TThostFtdcTradingSegmentSNType  TradingSegmentSN;
    ///进入本状态时间
    TThostFtdcTimeType  EnterTime;
    ///进入本状态原因
    TThostFtdcInstStatusEnterReasonType EnterReason;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>EnterTime：只有郑商所的时间戳是CTP的本地时间，其他交易所的是交易所时间</p>
<span class="anchor" id="a8f606a1-616f-4931-90f6-7592967f2b96"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b02ba14e-2d55-45ff-9f03-ce2ba3775338"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如何获取期权合约的状态？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>合约状态推送到产品级别，期权也是推送到产品级别。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
