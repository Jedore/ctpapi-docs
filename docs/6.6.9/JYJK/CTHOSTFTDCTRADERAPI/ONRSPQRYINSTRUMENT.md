<p>请求查询合约响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENT/">ReqQryInstrument</a>后，该方法被调用。</p>
<span class="anchor" id="e0f8616b-3ee0-4b47-b414-483cff67799b"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="938f76fd-8b58-412c-bb06-9115e9bec693"></span>
## 2.参数
<p>pInstrument：合约</p>
<pre><code>struct CThostFtdcInstrumentField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约名称
    TThostFtdcInstrumentNameType    InstrumentName;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve3;
    ///产品类型
    TThostFtdcProductClassType  ProductClass;
    ///交割年份
    TThostFtdcYearType  DeliveryYear;
    ///交割月
    TThostFtdcMonthType DeliveryMonth;
    ///市价单最大下单量
    TThostFtdcVolumeType    MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType    MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType    MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType    MinLimitOrderVolume;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType    VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///创建日
    TThostFtdcDateType  CreateDate;
    ///上市日
    TThostFtdcDateType  OpenDate;
    ///到期日
    TThostFtdcDateType  ExpireDate;
    ///开始交割日
    TThostFtdcDateType  StartDelivDate;
    ///结束交割日
    TThostFtdcDateType  EndDelivDate;
    ///合约生命周期状态
    TThostFtdcInstLifePhaseType InstLifePhase;
    ///当前是否交易
    TThostFtdcBoolType  IsTrading;
    ///持仓类型
    TThostFtdcPositionTypeType  PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType  PositionDateType;
    ///多头保证金率
    TThostFtdcRatioType LongMarginRatio;
    ///空头保证金率
    TThostFtdcRatioType ShortMarginRatio;
    ///是否使用大额单边保证金算法
    TThostFtdcMaxMarginSideAlgorithmType    MaxMarginSideAlgorithm;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve4;
    ///执行价
    TThostFtdcPriceType StrikePrice;
    ///期权类型
    TThostFtdcOptionsTypeType   OptionsType;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType    UnderlyingMultiple;
    ///组合类型
    TThostFtdcCombinationTypeType   CombinationType;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///产品代码
    TThostFtdcInstrumentIDType  ProductID;
    ///基础商品代码
    TThostFtdcInstrumentIDType  UnderlyingInstrID;
};
</code></pre>
<p>VolumeMultiple：合约乘数（同交易所）</p>
<p>PriceTick：最小变动价位（同交易所）</p>
<p>IsTrading：是否活跃（同交易所）</p>
<p>DeliveryYear：交割年份（同交易所）</p>
<p>DeliveryMonth：交割月（同交易所）</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>MaxMarketOrderVolume:（同交易所，郑商所的由柜台设置）</p>
<p><span alt="" id="anchor-id-02"></span> </p>
<p>MinMarketOrderVolume:（同交易所，市价单最小下单量来自柜台）</p>
<p>MaxLimitOrderVolume:（同交易所）</p>
<p>MinLimitOrderVolume:（同交易所）</p>
<blockquote>
<p>柜台版本6.6.5及以上版本支持每日从交易所更新市价单、限价单最大最小报单量；</p>
<p>CTP不会根据合约信息里的下单量限制去判断下单手数，交由交易所判断。</p>
</blockquote>
<p>OpenDate：上市日（同交易所）</p>
<p>CreateDate：创建日（同交易所）</p>
<p>ExpireDate：到期日（同交易所）</p>
<p>StartDeliveDate：开始交割日（同交易所）</p>
<p>EndDelivDate：结束交割日（同交易所）</p>
<blockquote>
<p><code>同交易所</code>表示这些字段每天更新自交易所，其余字段为柜台设置值。如果发现有些字段值有误，则以此来判断是否CTP柜台设置问题。</p>
</blockquote>
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
<span class="anchor" id="5a730daa-71e8-48ac-8124-54f60f601dd3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c014a30a-1b0a-4d62-9152-4085e0a069c9"></span>
## 4.FAQ
<p>无</p>
