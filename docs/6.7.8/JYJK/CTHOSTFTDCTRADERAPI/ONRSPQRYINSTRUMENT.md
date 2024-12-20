<p>请求查询合约响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENT/">ReqQryInstrument</a>后，该方法被调用。</p>
<span class="anchor" id="3c249469-203a-46d9-90e7-89adae469167"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d62d0706-5bdc-4a3d-b422-97b6de210df6"></span>
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
<p><span alt="" id="anchor-id-04"></span> </p>
<p>PositionDateType:持仓日期类型（区分产品是否有昨仓和今仓的区别，只有上海和能源是使用历史持仓）</p>
<p><span alt="" id="anchor-id-03"></span> </p>
<p>LongMarginRatio：多头保证金率（终值），算法如下：</p>
<p>跟随交易所多头保证金率：LongMarginRatioByMoney（由<a href="../ONRSPQRYEXCHANGEMARGINRATE/">OnRspQryExchangeMarginRate</a>查到）+LongMarginRatioByMoney（由<a href="../ONRSPQRYEXCHANGEMARGINRATEADJUST/">OnRspQryExchangeMarginRateAdjust</a>查到）</p>
<p>不跟随交易所多头保证金率：NoLongMarginRatioByMoney（由<a href="../ONRSPQRYEXCHANGEMARGINRATEADJUST/">OnRspQryExchangeMarginRateAdjust</a>查到）</p>
<p>ShortMarginRatio：空头保证金率（终值），算法如下：</p>
<p>跟随交易所空头保证金率：ShortMarginRatioByMoney（由<a href="../ONRSPQRYEXCHANGEMARGINRATE/">OnRspQryExchangeMarginRate</a>查到）+ShortMarginRatioByMoney（由<a href="../ONRSPQRYEXCHANGEMARGINRATEADJUST/">OnRspQryExchangeMarginRateAdjust</a>查到）</p>
<p>不跟随交易所空头保证金率：NoShortMarginRatioByMoney（由<a href="../ONRSPQRYEXCHANGEMARGINRATEADJUST/">OnRspQryExchangeMarginRateAdjust</a>查到）</p>
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
<span class="anchor" id="0f25b3c4-3137-4c4d-b0e3-2ebf96ffd8b2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="559a88bf-b025-4290-b339-6858305a12af"></span>
## 4.FAQ
<p>无</p>
